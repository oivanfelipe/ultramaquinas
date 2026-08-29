"""
Etapa 5 — Pesquisa Google + análise de gap dos 3 primeiros resultados orgânicos.
Usa Google Custom Search API para encontrar os concorrentes e extrai seu conteúdo.
"""

import requests
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import GOOGLE_API_KEY, GOOGLE_CSE_ID, SERP_RESULTS_TO_ANALYZE, REQUEST_TIMEOUT, FETCH_HEADERS

from bs4 import BeautifulSoup


def search_google(keyword: str, num_results: int = None) -> dict:
    """
    Busca o keyword no Google via Custom Search API.
    Retorna dict com: keyword, results (lista), error.
    Cada resultado: {title, url, snippet}
    """
    num_results = num_results or SERP_RESULTS_TO_ANALYZE

    result = {
        "keyword": keyword,
        "results": [],
        "error": None,
    }

    if not GOOGLE_CSE_ID:
        result["error"] = (
            "GOOGLE_CSE_ID não configurado. "
            "Crie um Custom Search Engine em https://cse.google.com e configure o ID em config.py"
        )
        return result

    if not GOOGLE_API_KEY:
        result["error"] = "GOOGLE_API_KEY não configurado em config.py"
        return result

    endpoint = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": GOOGLE_API_KEY,
        "cx": GOOGLE_CSE_ID,
        "q": keyword,
        "num": min(num_results, 10),
        "gl": "br",
        "hl": "pt-BR",
        "lr": "lang_pt",
    }

    try:
        resp = requests.get(endpoint, params=params, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        data = resp.json()
    except requests.RequestException as e:
        result["error"] = f"Erro na busca Google: {e}"
        return result

    items = data.get("items", [])
    if not items:
        result["error"] = "Nenhum resultado encontrado no Google para este keyword."
        return result

    for item in items[:num_results]:
        result["results"].append({
            "title": item.get("title", ""),
            "url": item.get("link", ""),
            "snippet": item.get("snippet", ""),
        })

    return result


def _extract_competitor_content(url: str, our_domain: str = "ultramaquinas.com.br") -> dict:
    """
    Baixa e extrai o conteúdo principal de uma URL concorrente.
    Ignora se for do próprio domínio.
    Retorna: {url, text, error}
    """
    result = {"url": url, "text": "", "error": None}

    if our_domain in url:
        result["error"] = "URL do próprio domínio — ignorada"
        return result

    try:
        resp = requests.get(url, headers=FETCH_HEADERS, timeout=REQUEST_TIMEOUT)
        resp.raise_for_status()
        html = resp.text
    except requests.RequestException as e:
        result["error"] = f"Erro ao acessar {url}: {e}"
        return result

    soup = BeautifulSoup(html, "lxml")

    # Remove ruído
    for tag in ["header", "footer", "nav", "script", "style", "noscript", "iframe", "aside"]:
        for el in soup.find_all(tag):
            el.decompose()

    noise_classes = [
        "breadcrumb", "breadcrumbs", "menu", "navigation", "sidebar",
        "cart", "checkout", "review", "reviews", "rating", "faq",
        "related", "cross-sell", "upsell", "similar", "newsletter",
        "cookie", "social", "share", "popup", "modal", "overlay",
    ]
    for cls in noise_classes:
        for el in soup.find_all(class_=lambda c: c and cls in " ".join(c).lower()):
            el.decompose()

    # Tenta localizar bloco principal de conteúdo
    content_block = (
        soup.find(attrs={"itemprop": "description"})
        or soup.find(class_=lambda c: c and any(
            kw in " ".join(c).lower()
            for kw in ["product-description", "description", "descricao", "product-detail", "pdp", "main-content"]
        ))
        or soup.find("main")
        or soup.find("article")
        or soup.find("body")
    )

    if content_block:
        text = content_block.get_text(separator="\n", strip=True)
    else:
        text = soup.get_text(separator="\n", strip=True)

    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    result["text"] = "\n".join(lines[:200])  # limita a 200 linhas para contexto razoável

    return result


def analyze_gap(our_content: str, competitor_texts: list[str], keyword: str) -> dict:
    """
    Identifica, de forma textual, os tópicos/ângulos presentes nos concorrentes
    mas ausentes (ou pouco enfatizados) no nosso conteúdo.
    Retorna: {gaps: list[str], competitor_count: int}

    Esta análise é heurística — a análise profunda fica a cargo do Claude.
    Aqui apenas extraímos e estruturamos os textos para enviar ao modelo.
    """
    return {
        "our_content_length": len(our_content.split()),
        "competitor_count": len(competitor_texts),
        "competitor_texts": competitor_texts,
    }


def run_serp_analysis(keyword: str, our_content: str) -> dict:
    """
    Executa a análise completa: busca Google → coleta conteúdo dos top 3 → estrutura gaps.
    Retorna dict com tudo que o optimizer precisa para o gap analysis.

    Retorna: {
        keyword, serp_results, competitor_contents, gap_context, error
    }
    """
    output = {
        "keyword": keyword,
        "serp_results": [],
        "competitor_contents": [],
        "gap_context": {},
        "error": None,
    }

    # Busca no Google
    serp = search_google(keyword)
    if serp["error"]:
        output["error"] = serp["error"]
        # Retorna sem gap analysis mas sem bloquear o pipeline
        return output

    output["serp_results"] = serp["results"]

    # Coleta conteúdo de cada resultado
    competitor_texts = []
    for item in serp["results"]:
        url = item["url"]
        content = _extract_competitor_content(url)
        if not content["error"] and content["text"]:
            competitor_texts.append({
                "url": url,
                "title": item["title"],
                "snippet": item["snippet"],
                "text": content["text"],
            })
        else:
            competitor_texts.append({
                "url": url,
                "title": item["title"],
                "snippet": item["snippet"],
                "text": item["snippet"],  # usa snippet como fallback
                "fetch_error": content["error"],
            })

    output["competitor_contents"] = competitor_texts

    # Estrutura o contexto de gap para o Claude
    output["gap_context"] = {
        "keyword": keyword,
        "our_word_count": len(our_content.split()),
        "competitors": [
            {
                "position": i + 1,
                "url": c["url"],
                "title": c["title"],
                "content_preview": c["text"][:1500] if c.get("text") else c.get("snippet", ""),
            }
            for i, c in enumerate(competitor_texts)
        ],
    }

    return output
