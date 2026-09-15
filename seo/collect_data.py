"""
Coleta dados do pipeline (fetch + GSC + SERP) sem chamar o Claude.
Salva resultado em output/dados_coletados.json para otimização manual.
Uso: python collect_data.py --file urls_verao.txt
"""

import argparse
import json
import os
import sys
import datetime

sys.path.insert(0, os.path.dirname(__file__))
from config import OUTPUT_DIR
from pipeline.fetcher import fetch_page_content
from pipeline.gsc import query_gsc, pick_keyword
from pipeline.serp import run_serp_analysis


def _log(msg):
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{ts}] {msg}", flush=True)


def collect(urls):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    results = []

    for i, url in enumerate(urls, 1):
        _log(f"\n{'='*60}")
        _log(f"URL {i}/{len(urls)}: {url}")

        entry = {"url": url, "fetch": {}, "gsc": {}, "keyword": {}, "serp": {}}

        # Fetch
        _log("  Etapa 1 — Fetch da página...")
        page_data = fetch_page_content(url)
        entry["fetch"] = page_data
        if page_data.get("error"):
            _log(f"  ERRO fetch: {page_data['error']}")
        else:
            _log(f"  Produto: {page_data.get('product_name')} ({len(page_data.get('text_content','').split())} palavras)")

        # GSC
        _log("  Etapa 2 — GSC...")
        gsc_data = query_gsc(url)
        entry["gsc"] = gsc_data
        if gsc_data.get("error"):
            _log(f"  AVISO GSC: {gsc_data['error']}")
        else:
            _log(f"  GSC: {gsc_data['total_clicks']} cliques, {len(gsc_data['queries'])} queries")

        # Keyword
        keyword_data = pick_keyword(gsc_data)
        keyword = keyword_data.get("query") or page_data.get("product_name", "")
        entry["keyword"] = {**keyword_data, "chosen": keyword}
        _log(f"  Keyword: \"{keyword}\" ({keyword_data.get('reason','')})")

        # SERP
        _log("  Etapa 3 — SERP...")
        serp = run_serp_analysis(keyword, page_data.get("text_content", ""))
        entry["serp"] = serp
        if serp.get("error"):
            _log(f"  AVISO SERP: {serp['error']}")
        else:
            _log(f"  SERP: {len(serp.get('competitor_contents',[]))} concorrentes")

        results.append(entry)

    out_path = os.path.join(OUTPUT_DIR, "dados_coletados.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    _log(f"\nDados salvos em: {out_path}")
    return out_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("urls", nargs="*")
    parser.add_argument("--file", "-f")
    args = parser.parse_args()

    urls = list(args.urls)
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            urls += [ln.strip() for ln in f if ln.strip() and not ln.startswith("#")]

    if not urls:
        parser.print_help()
        sys.exit(1)

    collect(urls)


if __name__ == "__main__":
    main()
