#!/usr/bin/env python3
"""Coleta os dados SEO mensais da Ultramáquinas via Composio (GSC + GA4).

Uso:
    export COMPOSIO_API_KEY=ak_...        # key Platform com permissão tool_execution (write)
    python3 scripts/composio_coletar.py 2026-09                 # GSC 'final' (padrão)
    python3 scripts/composio_coletar.py 2026-09 --data-state all  # inclui dias recentes (preliminar)

Grava dados/AAAA-MM.json. Só usa a biblioteca padrão. Nunca imprime a key.
"""
import argparse, calendar, json, os, sys, urllib.request

API = 'https://backend.composio.dev/api/v3.1'
SITE = os.environ.get('GSC_SITE_URL', 'https://www.ultramaquinas.com.br/')
GA4_PROPERTY = 'properties/' + os.environ.get('GA4_PROPERTY_ID', '326709572')
GA_METRICS = ['sessions', 'totalUsers', 'purchaseRevenue', 'transactions', 'addToCarts']
ORGANIC = {'filter': {'fieldName': 'sessionDefaultChannelGroup',
                      'stringFilter': {'matchType': 'EXACT', 'value': 'Organic Search'}}}


def call(method, path, key, body=None):
    req = urllib.request.Request(API + path, method=method, headers={'x-api-key': key, 'Content-Type': 'application/json'},
                                 data=json.dumps(body).encode() if body is not None else None)
    try:
        return json.load(urllib.request.urlopen(req, timeout=120))
    except urllib.error.HTTPError as e:
        sys.exit(f'Composio {e.code} em {path}: {e.read().decode()[:400]}')


def accounts(key):
    """Descobre as contas ativas (não depende de IDs fixos)."""
    out = {}
    for i in call('GET', '/connected_accounts?limit=100', key).get('items', []):
        if i.get('status') == 'ACTIVE':
            out[i['toolkit']['slug']] = (i['id'], i['user_id'])
    for t in ('google_search_console', 'google_analytics'):
        if t not in out:
            sys.exit(f'Conta {t} não está ACTIVE no Composio.')
    return out


def run(key, acc, toolkit, slug, args):
    cid, uid = acc[toolkit]
    r = call('POST', f'/tools/execute/{slug}', key, {'connected_account_id': cid, 'user_id': uid, 'arguments': args})
    if not r.get('successful', True):
        sys.exit(f'{slug} falhou: {json.dumps(r)[:400]}')
    return r.get('data', r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mes', help='AAAA-MM')
    ap.add_argument('--data-state', default='final', choices=['final', 'all'])
    a = ap.parse_args()
    key = os.environ.get('COMPOSIO_API_KEY') or sys.exit('Defina COMPOSIO_API_KEY (ver CLAUDE.md).')
    ano, mes = map(int, a.mes.split('-'))
    ini, fim = f'{a.mes}-01', f'{a.mes}-{calendar.monthrange(ano, mes)[1]:02d}'
    acc = accounts(key)

    def gsc(dims, n=25000):
        return run(key, acc, 'google_search_console', 'GOOGLE_SEARCH_CONSOLE_SEARCH_ANALYTICS_QUERY',
                   {'site_url': SITE, 'start_date': ini, 'end_date': fim, 'dimensions': dims,
                    'row_limit': n, 'data_state': a.data_state}).get('rows', [])

    def ga(dims, mets):
        return run(key, acc, 'google_analytics', 'GOOGLE_ANALYTICS_RUN_REPORT',
                   {'property': GA4_PROPERTY, 'dateRanges': [{'startDate': ini, 'endDate': fim}],
                    'metrics': [{'name': m} for m in mets], 'dimensions': [{'name': d} for d in dims],
                    'dimensionFilter': ORGANIC, 'limit': 1000}).get('rows', [])

    daily = sorted(gsc(['date']), key=lambda r: r['keys'][0])
    clicks = sum(r['clicks'] for r in daily)
    imp = sum(r['impressions'] for r in daily)
    pos = sum(r['position'] * r['impressions'] for r in daily) / imp   # posição ponderada por impressões
    tot = [float(x['value']) for x in ga([], GA_METRICS)[0]['metricValues']]
    rev_dia = {r['dimensionValues'][0]['value']: float(r['metricValues'][0]['value']) for r in ga(['date'], ['purchaseRevenue'])}
    dias = calendar.monthrange(ano, mes)[1]
    out = {
        'mes': a.mes, 'periodo': [ini, fim], 'data_state_gsc': a.data_state,
        'dias_gsc': len(daily), 'completo': len(daily) == dias and a.data_state == 'final',
        'gsc': {'cliques': clicks, 'impressoes': imp, 'ctr_pct': round(clicks / imp * 100, 4), 'posicao': round(pos, 4)},
        'ga4_organico': {'sessoes': int(tot[0]), 'usuarios': int(tot[1]), 'receita': round(tot[2], 2),
                         'pedidos': int(tot[3]), 'add_to_cart': int(tot[4])},
        'cliques_diarios': [r['clicks'] for r in daily],
        'receita_diaria': [round(rev_dia.get(f'{a.mes.replace("-", "")}{d:02d}', 0), 2) for d in range(1, dias + 1)],
        'top_keywords': [{'keyword': r['keys'][0], 'cliques': r['clicks'], 'impressoes': r['impressions'],
                          'ctr': r['ctr'], 'posicao': r['position']} for r in gsc(['query'], 100)[:50]],
        'top_paginas': [{'url': r['keys'][0], 'cliques': r['clicks'], 'impressoes': r['impressions'],
                         'ctr': r['ctr'], 'posicao': r['position']} for r in gsc(['page'], 100)[:50]],
    }
    os.makedirs('dados', exist_ok=True)
    path = f'dados/{a.mes}.json'
    json.dump(out, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(path, '|', 'completo' if out['completo'] else f'PARCIAL/PRELIMINAR ({len(daily)}/{dias} dias, {a.data_state})')
    print(out['gsc'], out['ga4_organico'])


if __name__ == '__main__':
    main()
