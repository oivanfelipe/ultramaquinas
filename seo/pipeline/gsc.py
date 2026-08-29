"""
Etapa 3 — Consulta ao Google Search Console via API direta.
Requer Service Account com acesso à propriedade no GSC.
"""

import json
import datetime
import requests
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import GSC_SERVICE_ACCOUNT_FILE, GSC_SITE_URL, GSC_DAYS_BACK, GSC_ROW_LIMIT


def _get_access_token(service_account_file: str) -> str:
    """
    Gera um access token usando Service Account (JWT flow).
    """
    import google.auth
    from google.oauth2 import service_account
    from google.auth.transport.requests import Request

    credentials = service_account.Credentials.from_service_account_file(
        service_account_file,
        scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
    )
    credentials.refresh(Request())
    return credentials.token


def query_gsc(url: str, site_url: str = None, days_back: int = None) -> dict:
    """
    Consulta o GSC para uma URL específica.
    Retorna dict com: url, queries (lista), error.

    Cada query: {query, clicks, impressions, ctr, position}
    """
    site_url = site_url or GSC_SITE_URL
    days_back = days_back or GSC_DAYS_BACK

    result = {
        "url": url,
        "queries": [],
        "total_clicks": 0,
        "total_impressions": 0,
        "avg_position": None,
        "error": None,
    }

    # Verifica se o arquivo de credenciais existe
    sa_file = GSC_SERVICE_ACCOUNT_FILE
    if not os.path.exists(sa_file):
        # Tenta caminho relativo ao diretório do script
        sa_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), GSC_SERVICE_ACCOUNT_FILE)
    if not os.path.exists(sa_file):
        result["error"] = (
            "Arquivo de credenciais GSC não encontrado. "
            f"Coloque o arquivo JSON do Service Account em: {GSC_SERVICE_ACCOUNT_FILE}"
        )
        return result

    try:
        token = _get_access_token(sa_file)
    except Exception as e:
        result["error"] = f"Erro ao autenticar no GSC: {e}"
        return result

    # Período de análise
    end_date = datetime.date.today() - datetime.timedelta(days=3)  # GSC tem delay de ~3 dias
    start_date = end_date - datetime.timedelta(days=days_back)

    endpoint = f"https://searchconsole.googleapis.com/webmasters/v3/sites/{requests.utils.quote(site_url, safe='')}/searchAnalytics/query"

    payload = {
        "startDate": start_date.isoformat(),
        "endDate": end_date.isoformat(),
        "dimensions": ["query"],
        "dimensionFilterGroups": [
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
        "rowLimit": GSC_ROW_LIMIT,
        "startRow": 0,
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }

    try:
        resp = requests.post(endpoint, json=payload, headers=headers, timeout=30)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        result["error"] = f"Erro na requisição GSC: {e}"
        return result

    rows = data.get("rows", [])
    if not rows:
        result["error"] = "Sem dados suficientes no Google Search Console para esta URL."
        return result

    queries = []
    for row in rows:
        keys = row.get("keys", [])
        queries.append({
            "query": keys[0] if keys else "",
            "clicks": row.get("clicks", 0),
            "impressions": row.get("impressions", 0),
            "ctr": round(row.get("ctr", 0) * 100, 2),
            "position": round(row.get("position", 0), 1),
        })

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
    Escolhe a keyword principal seguindo as regras de prioridade do ESPECIALISTA.
    Retorna: {keyword, reason, clicks, impressions, ctr, position}
    """
    queries = gsc_data.get("queries", [])
    if not queries:
        return {"keyword": None, "reason": "Sem dados GSC"}

    # Prioridade 1: maior número de cliques
    by_clicks = sorted(queries, key=lambda q: q["clicks"], reverse=True)
    if by_clicks[0]["clicks"] > 0:
        q = by_clicks[0]
        return {**q, "reason": "maior número de cliques"}

    # Prioridade 2: maior número de impressões
    by_impressions = sorted(queries, key=lambda q: q["impressions"], reverse=True)
    if by_impressions[0]["impressions"] > 0:
        q = by_impressions[0]
        return {**q, "reason": "maior número de impressões (cliques zerados)"}

    # Prioridade 3: posição entre 5 e 20 (maior potencial de crescimento)
    candidates = [q for q in queries if 5 <= q["position"] <= 20]
    if candidates:
        q = sorted(candidates, key=lambda q: q["impressions"], reverse=True)[0]
        return {**q, "reason": "posição entre 5-20 com maior potencial de crescimento"}

    return {"keyword": None, "reason": "Sem dados suficientes para escolha de keyword"}
