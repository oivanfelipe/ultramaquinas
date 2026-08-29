"""
Pipeline principal — SEO Optimizer Ultra Máquinas
Uso: python main.py <url> [url2 url3 ...]
     python main.py --file urls.txt
"""

import argparse
import json
import csv
import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(__file__))
from config import OUTPUT_DIR, OUTPUT_CSV, OUTPUT_JSON
from pipeline.fetcher import fetch_page_content
from pipeline.gsc import query_gsc, pick_keyword
from pipeline.serp import run_serp_analysis
from pipeline.optimizer import optimize


def _ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def _log(msg: str):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def process_url(url: str) -> dict:
    """
    Executa todas as etapas do pipeline para uma URL.
    Retorna o resultado final (dict com os campos do ESPECIALISTA ou error).
    """
    _log(f"Iniciando pipeline para: {url}")

    # Etapa 1: Fetch da página
    _log("  Etapa 1/4 — Buscando conteúdo da página...")
    page_data = fetch_page_content(url)
    if page_data.get("error"):
        _log(f"  ERRO no fetch: {page_data['error']}")
        return {"url": url, "error": page_data["error"], "stage": "fetch"}

    _log(f"  Produto: {page_data['product_name']} ({len(page_data['text_content'].split())} palavras extraídas)")

    # Etapa 2: Consulta GSC
    _log("  Etapa 2/4 — Consultando Google Search Console...")
    gsc_data = query_gsc(url)
    if gsc_data.get("error"):
        _log(f"  AVISO GSC: {gsc_data['error']}")
    else:
        _log(f"  GSC: {gsc_data['total_clicks']} cliques, {gsc_data['total_impressions']} impressões, {len(gsc_data['queries'])} queries")

    # Etapa 3: Escolha da keyword
    keyword_data = pick_keyword(gsc_data)
    keyword = keyword_data.get("query") or page_data.get("product_name", "")
    _log(f"  Keyword escolhida: \"{keyword}\" ({keyword_data.get('reason', '')})")

    # Etapa 4: SERP + gap analysis
    _log("  Etapa 3/4 — Analisando concorrentes no Google...")
    serp_result = run_serp_analysis(keyword, page_data.get("text_content", ""))
    if serp_result.get("error"):
        _log(f"  AVISO SERP: {serp_result['error']}")
    else:
        _log(f"  SERP: {len(serp_result.get('competitor_contents', []))} concorrentes analisados")

    # Etapa 5: Otimização via Claude
    _log("  Etapa 4/4 — Otimizando com Claude (ESPECIALISTA SÊNIOR)...")
    result = optimize(
        url=url,
        page_data=page_data,
        gsc_data=gsc_data,
        keyword_data=keyword_data,
        gap_context=serp_result.get("gap_context", {}),
    )

    if result.get("error"):
        _log(f"  ERRO na otimização: {result['error']}")
    else:
        _log(f"  Concluído — SEO Title: {result.get('seo_title', '')[:60]}")
        _log(f"  Word count: {result.get('word_count', '?')} palavras")

    return result


def run(urls: list[str]) -> list[dict]:
    _ensure_output_dir()
    results = []

    for i, url in enumerate(urls, 1):
        _log(f"\n{'='*60}")
        _log(f"URL {i}/{len(urls)}: {url}")
        _log('='*60)

        result = process_url(url)
        result["processed_at"] = datetime.datetime.now().isoformat()
        results.append(result)

    # Salva JSON
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    _log(f"\nJSON salvo em: {OUTPUT_JSON}")

    # Salva CSV (campos planos)
    csv_rows = []
    for r in results:
        descricao = r.get("descricao", {})
        csv_rows.append({
            "url": r.get("url", ""),
            "keyword_principal": r.get("keyword_principal", ""),
            "seo_title": r.get("seo_title", ""),
            "seo_title_chars": r.get("seo_title_chars", ""),
            "meta_description": r.get("meta_description", ""),
            "meta_description_chars": r.get("meta_description_chars", ""),
            "h2": descricao.get("h2", ""),
            "intro": descricao.get("intro", ""),
            "conclusao": descricao.get("conclusao", ""),
            "word_count": r.get("word_count", ""),
            "gaps_endereçados": "; ".join(r.get("gaps_endereçados", [])),
            "error": r.get("error", ""),
            "processed_at": r.get("processed_at", ""),
        })

    if csv_rows:
        with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=csv_rows[0].keys())
            writer.writeheader()
            writer.writerows(csv_rows)
        _log(f"CSV salvo em: {OUTPUT_CSV}")

    return results


def main():
    parser = argparse.ArgumentParser(
        description="SEO Optimizer — Ultra Máquinas",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python main.py https://www.ultramaquinas.com.br/produto/xyz
  python main.py https://url1.com https://url2.com
  python main.py --file urls.txt
        """,
    )
    parser.add_argument("urls", nargs="*", help="URLs dos produtos a otimizar")
    parser.add_argument("--file", "-f", help="Arquivo .txt com uma URL por linha")
    args = parser.parse_args()

    urls = list(args.urls)
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            file_urls = [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]
        urls.extend(file_urls)

    if not urls:
        parser.print_help()
        sys.exit(1)

    results = run(urls)

    errors = [r for r in results if r.get("error")]
    _log(f"\nResumo: {len(results) - len(errors)} sucesso(s), {len(errors)} erro(s)")

    if errors:
        _log("Erros:")
        for r in errors:
            _log(f"  {r['url']}: {r['error']}")


if __name__ == "__main__":
    main()
