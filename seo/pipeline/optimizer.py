"""
Etapa 6 — Otimização via Claude API.
Monta o prompt com todos os dados e chama o modelo ESPECIALISTA SÊNIOR.
"""

import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import CLAUDE_API_KEY, CLAUDE_MODEL

import anthropic


def _load_prompt(filename: str) -> str:
    prompts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "prompts")
    path = os.path.join(prompts_dir, filename)
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def _build_user_message(
    url: str,
    page_content: str,
    product_name: str,
    gsc_data: dict,
    keyword_data: dict,
    gap_context: dict,
) -> str:
    """
    Monta a mensagem de usuário com todos os dados do pipeline.
    """
    parts = []

    parts.append(f"## URL do Produto\n{url}")
    parts.append(f"## Nome do Produto\n{product_name}")

    parts.append("## Conteúdo da Página (extraído)")
    parts.append(page_content[:8000])  # limita para não estourar context window

    # Dados GSC
    parts.append("## Dados do Google Search Console")
    if gsc_data.get("error"):
        parts.append(f"Erro ao obter dados GSC: {gsc_data['error']}")
    else:
        parts.append(f"- Total de cliques: {gsc_data.get('total_clicks', 0)}")
        parts.append(f"- Total de impressões: {gsc_data.get('total_impressions', 0)}")
        parts.append(f"- Posição média: {gsc_data.get('avg_position', 'N/A')}")
        parts.append(f"\n### Queries (top {len(gsc_data.get('queries', []))})")
        for q in gsc_data.get("queries", [])[:20]:
            parts.append(
                f"- \"{q['query']}\" — {q['clicks']} cliques, "
                f"{q['impressions']} impressões, posição {q['position']}, CTR {q['ctr']}%"
            )

    # Keyword escolhida
    parts.append("## Keyword Principal Escolhida")
    if keyword_data.get("query"):
        parts.append(
            f"- Keyword: {keyword_data['query']}\n"
            f"- Critério: {keyword_data.get('reason', '')}\n"
            f"- Cliques: {keyword_data.get('clicks', 0)}\n"
            f"- Impressões: {keyword_data.get('impressions', 0)}\n"
            f"- Posição: {keyword_data.get('position', 'N/A')}"
        )
    else:
        parts.append(f"Sem keyword definida: {keyword_data.get('reason', 'dados insuficientes')}")

    # Gap de concorrentes
    parts.append("## Análise de Gap — Top 3 Resultados Orgânicos")
    if gap_context and gap_context.get("competitors"):
        for comp in gap_context["competitors"]:
            parts.append(f"\n### Posição {comp['position']}: {comp['title']}")
            parts.append(f"URL: {comp['url']}")
            parts.append(f"Conteúdo:\n{comp.get('content_preview', comp.get('snippet', ''))[:1000]}")
    else:
        parts.append("Análise de gap não disponível (CSE não configurado ou erro na busca).")

    # Tom de voz (incluído inline para garantia)
    tom = _load_prompt("tom_de_voz.md")
    parts.append(f"## Tom de Voz da Marca\n{tom}")

    return "\n\n".join(parts)


def optimize(
    url: str,
    page_data: dict,
    gsc_data: dict,
    keyword_data: dict,
    gap_context: dict,
) -> dict:
    """
    Chama o Claude com o prompt ESPECIALISTA SÊNIOR e retorna o JSON otimizado.
    Retorna: dict com os campos do ESPECIALISTA ou {error: str}.
    """
    if not CLAUDE_API_KEY:
        return {"error": "ANTHROPIC_API_KEY não configurada. Defina a variável de ambiente."}

    system_prompt = _load_prompt("especialista.md")

    user_message = _build_user_message(
        url=url,
        page_content=page_data.get("text_content", ""),
        product_name=page_data.get("product_name", ""),
        gsc_data=gsc_data,
        keyword_data=keyword_data,
        gap_context=gap_context,
    )

    client = anthropic.Anthropic(api_key=CLAUDE_API_KEY)

    try:
        response = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=4096,
            system=system_prompt,
            messages=[{"role": "user", "content": user_message}],
        )
    except anthropic.APIError as e:
        return {"error": f"Erro na API Claude: {e}"}

    raw = response.content[0].text.strip()

    # Remove possíveis markdown code fences
    if raw.startswith("```"):
        lines = raw.splitlines()
        raw = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])

    try:
        result = json.loads(raw)
    except json.JSONDecodeError as e:
        return {"error": f"Resposta do Claude não é JSON válido: {e}", "raw": raw}

    result["url"] = url
    return result
