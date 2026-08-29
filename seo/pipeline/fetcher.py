"""
Etapa 1 — Fetch e extração do conteúdo do produto.
Ignora header, footer, nav, scripts, CSS, reviews, FAQ, etc.
"""

import requests
from bs4 import BeautifulSoup
from typing import Optional
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import FETCH_HEADERS, REQUEST_TIMEOUT


# Tags e classes que devem ser removidas antes de extrair o conteúdo
_REMOVE_TAGS = [
    "header", "footer", "nav", "script", "style", "noscript",
    "iframe", "aside",
]

_REMOVE_CLASSES = [
    "breadcrumb", "breadcrumbs", "popup", "modal", "overlay",
    "review", "reviews", "rating", "faq", "related", "cross-sell",
    "upsell", "similar", "recommended", "newsletter", "cookie",
    "social", "share", "header", "footer", "navigation", "menu",
    "sidebar", "cart", "checkout",
]


def fetch_page_content(url: str) -> dict:
    """
    Faz o download da página e extrai apenas o conteúdo relevante do produto.
    Retorna dict com: url, html_raw, text_content, product_name, status_code.
    """
    result = {
        "url": url,
        "html_raw": "",
        "text_content": "",
        "product_name": "",
        "status_code": None,
        "error": None,
    }

    try:
        resp = requests.get(url, headers=FETCH_HEADERS, timeout=REQUEST_TIMEOUT)
        result["status_code"] = resp.status_code
        resp.raise_for_status()
        result["html_raw"] = resp.text
    except requests.RequestException as e:
        result["error"] = f"Erro ao acessar a URL: {e}"
        return result

    soup = BeautifulSoup(result["html_raw"], "lxml")

    # Extrai o nome do produto do <title> ou <h1>
    title_tag = soup.find("title")
    h1_tag = soup.find("h1")
    if h1_tag:
        result["product_name"] = h1_tag.get_text(strip=True)
    elif title_tag:
        result["product_name"] = title_tag.get_text(strip=True).split("|")[0].strip()

    # Remove tags indesejadas
    for tag in _REMOVE_TAGS:
        for el in soup.find_all(tag):
            el.decompose()

    # Remove elementos por classe
    for cls in _REMOVE_CLASSES:
        for el in soup.find_all(class_=lambda c: c and cls in " ".join(c).lower()):
            el.decompose()

    # Tenta localizar o bloco principal do produto
    # Prioridade: [itemprop=description], .product-description, .descricao, .description, main, body
    content_block = (
        soup.find(attrs={"itemprop": "description"})
        or soup.find(class_=lambda c: c and any(
            kw in " ".join(c).lower()
            for kw in ["product-description", "descricao", "description", "product-detail", "pdp"]
        ))
        or soup.find("main")
        or soup.find("body")
    )

    if content_block:
        # Remove elementos filhos com classes de ruído dentro do bloco
        for cls in _REMOVE_CLASSES:
            for el in content_block.find_all(class_=lambda c: c and cls in " ".join(c).lower()):
                el.decompose()
        result["text_content"] = content_block.get_text(separator="\n", strip=True)
    else:
        result["text_content"] = soup.get_text(separator="\n", strip=True)

    # Limpa linhas em branco excessivas
    lines = [ln.strip() for ln in result["text_content"].splitlines() if ln.strip()]
    result["text_content"] = "\n".join(lines)

    return result
