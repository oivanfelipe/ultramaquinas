"""
Etapa 2 — Consulta ao Google Search Console via Composio v3.1.
Fallback: autenticação direta com Service Account quando Composio não estiver configurado.
"""

import datetime
import os
import sys
import requests

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import (
    COMPOSIO_API_KEY,
    COMPOSIO_BASE_URL,
    COMPOSIO_GSC_ACCOUNT_ID,
    COMPOSIO_ENTITY_ID,
    GSC_SERVICE_ACCOUNT_FILE,
    GSC_SITE_URL,
    GSC_DAYS_BACK,
    GSC_ROW_LIMIT,
)

# ─── Composio v3.1 ────────────────────────────────────────────────────────────

_COMPOSIO_ACTION = "GOOGLE_SEARCH_CONSOLE_SEARCH_ANALYTICS_QUERY"


def _query_via_composio(url: str, site_url: str, start_date: str, end_date: str) -> list:
    """
    Consulta o GSC via Composio v3.1 REST API.
    Retorna lista de rows GSC ou raises RuntimeError em caso de falha.
    """
    endpoint = f"{COMPOSIO_BASE_URL}/tools/execute/{_COMPOSIO_ACTION}"
    headers = {
        "x-api-key": COMPOSIO_API_KEY,
        "Content-Type": "application/json",
    }
    body = {
        "connected_account_id": COMPOSIO_GSC_ACCOUNT_ID,
        "entity_id": COMPOSIO_ENTITY_ID,
        "arguments": {
            "site_url": site_url,
            "start_date": start_date,
            "end_date": end_date,
            "dimensions": ["query"],
            "row_limit": GSC_ROW_LIMIT,
            "dimension_filter_groups": [
                {
                    "filters": [
                        {
                            "dimension": "page",
                            "operator": "equals",
                            "expression": url,
                        }
                    ]
                }
            ],
        },
    }

    resp = requests.post(endpoint, json=body, headers=headers, timeout=30)

    try:
        data = resp.json()
    except Exception:
        raise RuntimeError(f"Composio retornou resposta inválida (HTTP {resp.status_code})")

    if not resp.ok or not data.get("successful"):
        err = data.get("error") or data.get("message") or str(data)
        raise RuntimeError(f"Composio erro: {err}")

    return data.get("data", {}).get("rows", [])


# ─── Fallback: Service Account direto ────────────────────────────────────────

def _get_sa_token(sa_file: str) -> str:
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request

    creds = service_account.Credentials.from_service_account_file(
        sa_file,
        scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
    )
    creds.refresh(Request())
    return creds.token


def _query_via_service_account(
    url: str, site_url: str, start_date: str, end_date: str, sa_file: str
) -> list:
    token = _get_sa_token(sa_file)
    endpoint = (
        "https://searchconsole.googleapis.com/webmasters/v3/sites/"
        + requests.utils.quote(site_url, safe="")
        + "/searchAnalytics/query"
    )
    payload = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["query"],
        "dimensionFilterGroups": [
            {
                "filters": [
                    {"dimension": "page", "operator": "equals", "expression": url}
                ]
            }
        ],
        "rowLimit": GSC_ROW_LIMIT,
        "startRow": 0,
    }
    resp = requests.post(
        endpoint,
        json=payload,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
        timeout=30,
    )
    resp.raise_for_status()
    return resp.json().get("rows", [])


# ─── Interface pública ────────────────────────────────────────────────────────

def query_gsc(url: str, site_url: str = None, days_back: int = None) -> dict:
    """
    Consulta o GSC para uma URL específica.
    Tenta Composio primeiro; faz fallback para Service Account se necessário.

    Retorna: {url, queries, total_clicks, total_impressions, avg_position, error, source}
    Cada query: {query, clicks, impressions, ctr, position}
    """
    site_url = site_url or GSC_SITE_URL
    days_back = days_back or GSC_DAYS_BACK

    end_date = (datetime.date.today() - datetime.timedelta(days=3)).isoformat()
    start_date = (
        datetime.date.today() - datetime.timedelta(days=days_back + 3)
    ).isoformat()

    result = {
        "url": url,
        "queries": [],
        "total_clicks": 0,
        "total_impressions": 0,
        "avg_position": None,
        "error": None,
        "source": None,
    }

    rows = None

    # 1. Tenta Composio
    if COMPOSIO_API_KEY and COMPOSIO_GSC_ACCOUNT_ID and COMPOSIO_ENTITY_ID:
        try:
            rows = _query_via_composio(url, site_url, start_date, end_date)
            result["source"] = "composio"
        except Exception as e:
            result["error"] = f"Composio falhou: {e}"
            rows = None
    else:
        missing = [
            k for k, v in {
                "COMPOSIO_API_KEY": COMPOSIO_API_KEY,
                "COMPOSIO_GSC_ACCOUNT_ID": COMPOSIO_GSC_ACCOUNT_ID,
                "COMPOSIO_ENTITY_ID": COMPOSIO_ENTITY_ID,
            }.items() if not v
        ]
        result["error"] = f"Composio não configurado ({', '.join(missing)})"

    # 2. Fallback: Service Account
    if rows is None:
        sa_file = GSC_SERVICE_ACCOUNT_FILE
        if not os.path.isabs(sa_file):
            sa_alt = os.path.join(os.path.dirname(os.path.dirname(__file__)), sa_file)
            if os.path.exists(sa_alt):
                sa_file = sa_alt

        if os.path.exists(sa_file):
            try:
                rows = _query_via_service_account(url, site_url, start_date, end_date, sa_file)
                result["source"] = "service_account"
                result["error"] = None
            except Exception as e:
                prev = result["error"] or ""
                result["error"] = f"{prev} | SA fallback falhou: {e}".lstrip(" |")
                rows = []
        else:
            prev = result["error"] or ""
            result["error"] = (
                f"{prev} | Arquivo SA não encontrado: {GSC_SERVICE_ACCOUNT_FILE}"
            ).lstrip(" |")
            rows = []

    if not rows:
        if not result["error"]:
            result["error"] = "Sem dados no Google Search Console para esta URL."
        return result

    queries = []
    for row in rows:
        keys = row.get("keys", [])
        queries.append(
            {
                "query": keys[0] if keys else "",
                "clicks": row.get("clicks", 0),
                "impressions": row.get("impressions", 0),
                "ctr": round(row.get("ctr", 0) * 100, 2),
                "position": round(row.get("position", 0), 1),
            }
        )

    result["queries"] = queries
    result["total_clicks"] = sum(q["clicks"] for q in queries)
    result["total_impressions"] = sum(q["impressions"] for q in queries)
    if queries:
        result["avg_position"] = round(
            sum(q["position"] for q in queries) / len(queries), 1
        )

    return result


def pick_keyword(gsc_data: dict) -> dict:
    """
    Escolhe a keyword principal pelas regras do ESPECIALISTA.
    Retorna: {query, reason, clicks, impressions, ctr, position}
    """
    queries = gsc_data.get("queries", [])
    if not queries:
        return {"keyword": None, "reason": "Sem dados GSC"}

    by_clicks = sorted(queries, key=lambda q: q["clicks"], reverse=True)
    if by_clicks[0]["clicks"] > 0:
        return {**by_clicks[0], "reason": "maior número de cliques"}

    by_impressions = sorted(queries, key=lambda q: q["impressions"], reverse=True)
    if by_impressions[0]["impressions"] > 0:
        return {**by_impressions[0], "reason": "maior número de impressões (cliques zerados)"}

    candidates = [q for q in queries if 5 <= q["position"] <= 20]
    if candidates:
        q = sorted(candidates, key=lambda q: q["impressions"], reverse=True)[0]
        return {**q, "reason": "posição entre 5-20 com maior potencial de crescimento"}

    return {"keyword": None, "reason": "Sem dados suficientes para escolha de keyword"}
