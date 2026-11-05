#!/usr/bin/env python3
"""Gera a aba de um mês no index.html a partir de dados/AAAA-MM.json (coletado via Composio).

Uso:  python3 scripts/gerar_aba_mes.py 2026-10            # compara com o mês anterior, grava em index.html
      python3 scripts/gerar_aba_mes.py 2026-09 --index velho.html --out novo.html   # teste

Cria: botão em .tabs-nav, bloco <div id="tab-xxx">, IIFE de gráficos. A aba nova vira a ativa.
Pré-requisitos: dados/AAAA-MM.json completo e dados/<mês anterior>.json.
"""
import argparse, json, os, re
from datetime import date

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOMES = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
ABR = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
ID = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
# cor por mês (rgb). Ago e Set mantêm as cores já publicadas.
COR = {8: '204,0,0', 9: '30,90,180', 10: '224,123,0', 11: '27,127,62', 12: '120,60,160'}
# Base publicada Jan–Ago/2026 (a barra "Jan/Fev*" entra duas vezes no YTD) — ver COMPOSIO.md
BASE = dict(cliques=[10957, 11228, 9719, 9181, 9186, 9339, 9571], impressoes=[1941101, 1960672, 1624785, 1647751, 1619624, 1357607, 1689302],
            receita=[35753, 38074, 35314, 22926, 31253, 19413, 34379], pedidos=[100, 68, 99, 55, 83, 71, 64])
YTD_AGO = dict(cliques=80138, impressoes=13781942, receita=252866, pedidos=640, sessoes=93539)
BASE_COLS = ['180,180,180,0.85', '130,130,130,0.85', '80,80,80,0.85', '204,0,0,0.70', '26,26,26,0.85', '27,127,62,0.85', '204,0,0,0.85']


def n(v): return f"{int(round(v)):,}".replace(',', '.')
def dec(v, k=2): return f"{v:.{k}f}".replace('.', ',')
def sgn(v, k=1): return ('' if round(abs(v), k) == 0 else '+' if v > 0 else '-') + dec(abs(v), k)
def pc(c, p): return (c / p - 1) * 100
def R(v): return 'R$' + n(v)
def carrega(mes): return json.load(open(os.path.join(RAIZ, 'dados', f'{mes}.json'), encoding='utf-8'))


def metricas(D):
    g, a = D['gsc'], D['ga4_organico']
    m = dict(cliques=g['cliques'], imp=g['impressoes'], ctr=g['cliques'] / g['impressoes'] * 100, pos=g['posicao'], sess=a['sessoes'],
             users=a['usuarios'], rev=a['receita'], orders=a['pedidos'], atc=a['add_to_cart'])
    m['tick'] = m['rev'] / m['orders'] if m['orders'] else 0
    m['conv'] = m['orders'] / m['sess'] * 100
    return m


def delta(kind, cur, prev, good_up=True):
    if kind == 'pct': d = pc(cur, prev); txt = f"{sgn(d)}%"
    elif kind == 'pp': d = cur - prev; txt = f"{sgn(d, 2)} pp"
    else: d = prev - cur; txt = f"{sgn(d, 2)} pos"      # posição: menor = melhor
    if kind != 'pct' and abs(d) < 0.005: return 'neutral', '▬', txt
    better = d > 0 if kind == 'pos' else ((d > 0) == good_up)
    return ('up' if better else 'down'), ('▲' if d > 0 else '▼'), txt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('mes')
    ap.add_argument('--index', default=os.path.join(RAIZ, 'index.html'))
    ap.add_argument('--out')
    a = ap.parse_args()
    ano, mm = map(int, a.mes.split('-'))
    pa, pm = (ano, mm - 1) if mm > 1 else (ano - 1, 12)
    prev_mes = f'{pa}-{pm:02d}'
    D, P = carrega(a.mes), carrega(prev_mes)
    assert D['completo'], f'{a.mes} ainda não está completo no GSC'
    M, Pm = metricas(D), metricas(P)
    sfx, psfx, nome, pnome, ab, pab = ID[mm - 1], ID[pm - 1], NOMES[mm - 1], NOMES[pm - 1], ABR[mm - 1], ABR[pm - 1]
    dias = len(D['cliques_diarios'])
    cur_rgb, prev_rgb = COR.get(mm, '60,60,60'), COR.get(pm, '60,60,60')

    def sc(label, val, key, kind='pct', fmt=n):
        cls, ar, txt = delta(kind, M[key], Pm[key])
        return (f'    <div class="scorecard {"up" if cls == "up" else "down"}">\n      <div class="scorecard-label">{label}</div>\n'
                f'      <div class="scorecard-value">{val}</div>\n      <span class="scorecard-delta {cls}">{ar} {txt} vs {pab}</span>\n'
                f'      <div class="scorecard-prev">{pab}: {fmt(Pm[key])}</div>\n    </div>\n')

    def row(label, key, kind='pct', fmt=n):
        cls, ar, txt = delta(kind, M[key], Pm[key])
        return f'        <tr><td>{label}</td><td class="num">{fmt(M[key])}</td><td class="num">{fmt(Pm[key])}</td><td class="tag-{cls}">{ar} {txt}</td></tr>\n'
    pct2 = lambda v: dec(v) + '%'
    cards = (sc('Cliques Orgânicos', n(M['cliques']), 'cliques') + sc('Impressões Orgânicas', n(M['imp']), 'imp') +
             sc('CTR Orgânico', pct2(M['ctr']), 'ctr', 'pp', pct2) + sc('Posição Média', dec(M['pos']), 'pos', 'pos', dec) +
             sc('Receita Orgânica', R(M['rev']), 'rev', fmt=R))
    rows = (row('Cliques Orgânicos', 'cliques') + row('Impressões Orgânicas', 'imp') + row('CTR Orgânico', 'ctr', 'pp', pct2) +
            row('Posição Média', 'pos', 'pos', dec) + row('Sessões Orgânicas', 'sess') + row('Usuários Orgânicos', 'users') +
            row('Receita Orgânica', 'rev', fmt=R) + row('Pedidos Orgânicos', 'orders', fmt=str) + row('Ticket Médio', 'tick', fmt=R))
    cards6 = (sc('Receita Orgânica', R(M['rev']), 'rev', fmt=R) + sc('Pedidos Orgânicos', str(M['orders']), 'orders', fmt=str) +
              sc('Ticket Médio', R(M['tick']), 'tick', fmt=R) + sc('Add-to-Carts', n(M['atc']), 'atc') +
              sc('Sessões Orgânicas', n(M['sess']), 'sess') + sc('Taxa de Conversão', pct2(M['conv']), 'conv', 'pp', pct2))

    # --- acumulado: base Jan–Ago + meses de Set até o mês atual
    meses_extra = [f'{ano}-{m:02d}' for m in range(9, mm + 1)]
    ex = [metricas(carrega(x)) for x in meses_extra]
    ytd = dict(cliques=YTD_AGO['cliques'] + sum(e['cliques'] for e in ex), imp=YTD_AGO['impressoes'] + sum(e['imp'] for e in ex),
               rev=YTD_AGO['receita'] + sum(e['rev'] for e in ex), orders=YTD_AGO['pedidos'] + sum(e['orders'] for e in ex),
               sess=YTD_AGO['sessoes'] + sum(e['sess'] for e in ex))
    nmeses = mm
    card = lambda lab, v, sub: f'    <div class="ytd-card">\n      <div class="ytd-card-label">{lab}</div>\n      <div class="ytd-card-value">{v}</div>\n      <div class="ytd-card-sub">{sub}</div>\n    </div>\n'
    ytdhtml = (card('Cliques Orgânicos YTD', n(ytd['cliques']), 'Média mensal: ' + n(ytd['cliques'] / nmeses)) +
               card('Impressões YTD', n(ytd['imp']), 'Média mensal: ' + n(ytd['imp'] / nmeses)) +
               card('Receita Orgânica YTD', R(ytd['rev']), 'Média mensal: ' + R(ytd['rev'] / nmeses)) +
               card('Pedidos Orgânicos YTD', n(ytd['orders']), 'Média mensal: ' + n(ytd['orders'] / nmeses)) +
               card('Sessões Orgânicas YTD', n(ytd['sess']), 'Média mensal: ' + n(ytd['sess'] / nmeses)) +
               card('Ticket Médio YTD', R(ytd['rev'] / ytd['orders']), f"Total: {ytd['orders']} pedidos"))

    kw = ''.join(f'<tr><td>{i}</td><td>{k["keyword"]}</td><td class="num">{k["cliques"]}</td><td class="num">{n(k["impressoes"])}</td><td class="num">{k["ctr"] * 100:.2f}%</td><td class="num">{k["posicao"]:.2f}</td></tr>\n'
                 for i, k in enumerate(D['top_keywords'][:20], 1))

    def path(u):
        p = re.sub(r'^https?://[^/]+', '', u)
        return '/ (Home)' if p in ('', '/') else (p if len(p) <= 46 else p[:45] + '…')
    pg = ''.join(f'<tr><td>{i}</td><td class="url">{path(k["url"])}</td><td class="num">{k["cliques"]}</td><td class="num">{n(k["impressoes"])}</td><td class="num">{k["ctr"] * 100:.2f}%</td><td class="num">{k["posicao"]:.2f}</td></tr>\n'
                 for i, k in enumerate(D['top_paginas'][:15], 1))

    # --- insight factual (sem adjetivos de intensidade)
    insight = (f"{nome} fechou com cliques em {sgn(pc(M['cliques'], Pm['cliques']))}% e impressões em {sgn(pc(M['imp'], Pm['imp']))}% em relação a {pnome}, "
               f"com CTR de {pct2(M['ctr'])} ({sgn(M['ctr'] - Pm['ctr'], 2)} pp) e posição média de {dec(M['pos'])} ({sgn(Pm['pos'] - M['pos'], 2)} pos). "
               f"No site, as sessões orgânicas variaram {sgn(pc(M['sess'], Pm['sess']))}% e os usuários {sgn(pc(M['users'], Pm['users']))}%. "
               f"A receita orgânica foi de {R(M['rev'])} ({sgn(pc(M['rev'], Pm['rev']))}%), com {M['orders']} pedidos ({sgn(pc(M['orders'], Pm['orders']))}%) "
               f"e ticket médio de {R(M['tick'])} ({sgn(pc(M['tick'], Pm['tick']))}%). "
               f"A taxa de conversão ficou em {pct2(M['conv'])} ({sgn(M['conv'] - Pm['conv'], 2)} pp) e os add-to-carts em {n(M['atc'])} ({sgn(pc(M['atc'], Pm['atc']))}%).")

    hoje = date.today()
    gerado, gerado_n = f"{hoje.day:02d} {ABR[hoje.month - 1]} {hoje.year}", hoje.strftime('%d/%m/%Y')
    ult = f"{dias:02d}"
    html = f'''<div id="tab-{sfx}" class="tab-content active">

<div class="header">
  <div class="header-tag">// SEO Performance Report · Jan–{ab} {ano}</div>
  <h1>Ultramáquinas<br><span>Relatório SEO</span> — {nome} {ano}</h1>
  <div class="header-meta">
    <div class="header-meta-item">Período atual <strong>01–{ult} {ab} {ano}</strong></div>
    <div class="header-meta-item">Comparativo <strong>{pab} {ano}</strong></div>
    <div class="header-meta-item">Acumulado <strong>Jan–{ab} {ano}</strong></div>
    <div class="header-meta-item">Domínio <strong>ultramaquinas.com.br</strong></div>
    <div class="header-meta-item">Gerado em <strong>{gerado}</strong></div>
  </div>
</div>

<nav class="nav">
  <a href="#resumo-{sfx}">01 Resumo</a>
  <a href="#performance-{sfx}">02 Performance</a>
  <a href="#ytd-{sfx}">03 Acumulado YTD</a>
  <a href="#keywords-{sfx}">04 Keywords</a>
  <a href="#paginas-{sfx}">05 Páginas</a>
  <a href="#receita-{sfx}">06 Receita</a>
</nav>

<div class="container">

<!-- 01 RESUMO -->
<section class="section" id="resumo-{sfx}">
  <div class="section-label">01</div>
  <div class="section-title">Resumo <span>Executivo</span></div>
  <div class="scorecard-grid">
{cards}  </div>

  <div class="insight-box">
    <p>{insight}</p>
  </div>

  <div class="table-wrap">
    <table>
      <thead><tr><th>Métrica</th><th>{nome} {ano}</th><th>{pnome} {ano}</th><th>{ab} vs {pab}</th></tr></thead>
      <tbody>
{rows}      </tbody>
    </table>
  </div>
</section>

<!-- 02 PERFORMANCE -->
<section class="section" id="performance-{sfx}">
  <div class="section-label">02</div>
  <div class="section-title">Performance <span>Orgânica</span></div>
  <div class="charts-row">
    <div class="chart-block" style="flex:2">
      <div class="chart-title">Cliques Diários — {pab} vs {ab} {ano}</div>
      <canvas id="chartClicksDaily-{sfx}" height="120"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">CTR Orgânico</div>
      <canvas id="chartCTR-{sfx}" height="120"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">Posição Média</div>
      <canvas id="chartPosition-{sfx}" height="120"></canvas>
    </div>
  </div>
</section>

<!-- 03 YTD -->
<section class="section" id="ytd-{sfx}">
  <div class="section-label">03</div>
  <div class="section-title">Acumulado <span>Jan–{ab} {ano}</span></div>
  <div class="ytd-cards">
{ytdhtml}  </div>
  <div class="charts-row">
    <div class="chart-block">
      <div class="chart-title">Cliques por Mês (YTD)</div>
      <canvas id="chartClicksYTD-{sfx}" height="130"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">Impressões por Mês (YTD)</div>
      <canvas id="chartImpYTD-{sfx}" height="130"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">Receita por Mês (YTD)</div>
      <canvas id="chartRevYTD-{sfx}" height="130"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">Pedidos por Mês (YTD)</div>
      <canvas id="chartOrdYTD-{sfx}" height="130"></canvas>
    </div>
  </div>
</section>

<!-- 04 KEYWORDS -->
<section class="section" id="keywords-{sfx}">
  <div class="section-label">04</div>
  <div class="section-title">Análise de <span>Palavras-chave</span></div>
  <p class="section-desc">Top 20 keywords por cliques orgânicos — {nome} {ano} · Google Search Console</p>
  <div class="table-wrap">
    <table>
      <thead><tr><th>#</th><th>Keyword</th><th>Cliques</th><th>Impressões</th><th>CTR</th><th>Posição</th></tr></thead>
      <tbody>
{kw}
      </tbody>
    </table>
  </div>
</section>

<!-- 05 PÁGINAS -->
<section class="section" id="paginas-{sfx}">
  <div class="section-label">05</div>
  <div class="section-title">Páginas com Melhor <span>Desempenho</span></div>
  <p class="section-desc">Top 15 páginas por cliques orgânicos — {nome} {ano} · Google Search Console</p>
  <div class="table-wrap">
    <table>
      <thead><tr><th>#</th><th>Página</th><th>Cliques</th><th>Impressões</th><th>CTR</th><th>Posição</th></tr></thead>
      <tbody>
{pg}
      </tbody>
    </table>
  </div>
</section>

<!-- 06 RECEITA -->
<section class="section" id="receita-{sfx}">
  <div class="section-label">06</div>
  <div class="section-title">Faturamento <span>Orgânico</span></div>
  <div class="scorecard-grid">
{cards6}  </div>
  <div class="chart-wide">
    <div class="chart-title">Receita Orgânica Diária — {pab} vs {ab} {ano}</div>
    <canvas id="chartRevDaily-{sfx}"></canvas>
  </div>
</section>

</div>

<div class="footer">
  <span>Dados: Google Search Console · Google Analytics 4 (Tráfego Orgânico) · via Composio</span>
  <span>Ultramáquinas · Relatório SEO {nome} {ano} · Gerado em {gerado_n}</span>
</div>

</div>

'''
    # --- JS
    J = lambda v: json.dumps(v)
    meses_lbl = ['Jan/Fev*', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago'] + [ABR[m - 1] for m in range(9, mm + 1)]
    cols = BASE_COLS + [f'{COR.get(m, "60,60,60")},0.85' for m in range(9, mm + 1)]
    cols_js = '[' + ','.join(f"'rgba({c})'" for c in cols) + ']'
    ser = lambda base, key: base + [round(e[key]) if key == 'rev' else e[key] for e in ex]
    ctr_lo, ctr_hi = int((min(M['ctr'], Pm['ctr']) - 0.1) * 20) / 20, -int(-(max(M['ctr'], Pm['ctr']) + 0.1) * 20) // 1 / 20
    pos_lo, pos_hi = int((min(M['pos'], Pm['pos']) - 0.4) * 2) / 2, -int(-(max(M['pos'], Pm['pos']) + 0.4) * 2) // 1 / 2
    pad = lambda arr: arr + [None] * (31 - len(arr))
    leg = "plugins:{legend:{display:true,labels:{color:'#555',boxWidth:10,font:{size:10,family:'Montserrat'}}}"
    js = f'''(function(){{
const grid_s='rgba(0,0,0,0.06)';
const baseOpts_s={{responsive:true,maintainAspectRatio:true,plugins:{{legend:{{display:false}}}},scales:{{x:{{grid:{{color:grid_s}},ticks:{{color:'#aaa',maxTicksLimit:8}}}},y:{{grid:{{color:grid_s}},ticks:{{color:'#aaa',maxTicksLimit:5}}}}}}}};
const C_PREV_S='rgba({prev_rgb},0.85)',C_CUR_S='rgba({cur_rgb},0.85)';
const C_PREV_LS='rgba({prev_rgb},0.12)',C_CUR_LS='rgba({cur_rgb},0.12)';
const cliqPrev_s={J(P['cliques_diarios'])};
const cliqCur_s={J(D['cliques_diarios'])};
const dias31_s=Array.from({{length:31}},(_,i)=>i+1);
const pad_s=(arr,n)=>[...arr,...Array(Math.max(0,n-arr.length)).fill(null)];
new Chart(document.getElementById('chartClicksDaily-{sfx}'),{{type:'line',data:{{labels:dias31_s,datasets:[
  {{label:'{pab}',data:pad_s(cliqPrev_s,31),borderColor:C_PREV_S,backgroundColor:C_PREV_LS,tension:.3,pointRadius:0,borderWidth:2,fill:false}},
  {{label:'{ab}',data:pad_s(cliqCur_s,31),borderColor:C_CUR_S,backgroundColor:C_CUR_LS,tension:.3,pointRadius:0,borderWidth:2,fill:false}}
]}},options:{{...baseOpts_s,{leg}}}}}}});
new Chart(document.getElementById('chartCTR-{sfx}'),{{type:'bar',data:{{labels:['{pab} {ano}','{ab} {ano}'],datasets:[{{data:[{Pm['ctr']:.2f},{M['ctr']:.2f}],backgroundColor:[C_PREV_S,C_CUR_S],borderRadius:3,borderSkipped:false}}]}},options:{{...baseOpts_s,plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{label:c=>` ${{c.raw.toFixed(2)}}%`}}}}}},scales:{{...baseOpts_s.scales,y:{{...baseOpts_s.scales.y,min:{ctr_lo},max:{ctr_hi},ticks:{{callback:v=>v.toFixed(2)+'%',color:'#555',maxTicksLimit:5}}}}}}}}}});
new Chart(document.getElementById('chartPosition-{sfx}'),{{type:'bar',data:{{labels:['{pab} {ano}','{ab} {ano}'],datasets:[{{data:[{Pm['pos']:.2f},{M['pos']:.2f}],backgroundColor:[C_PREV_S,C_CUR_S],borderRadius:3,borderSkipped:false}}]}},options:{{...baseOpts_s,plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{label:c=>` ${{c.raw.toFixed(2)}}`}}}}}},scales:{{...baseOpts_s.scales,y:{{...baseOpts_s.scales.y,min:{pos_lo},max:{pos_hi},ticks:{{callback:v=>v.toFixed(2),color:'#555',maxTicksLimit:5}}}}}}}}}});
const mesesYTD_s={J(meses_lbl)};
const colsYTD_s={cols_js};
new Chart(document.getElementById('chartClicksYTD-{sfx}'),{{type:'bar',data:{{labels:mesesYTD_s,datasets:[{{data:{J(ser(BASE['cliques'], 'cliques'))},backgroundColor:colsYTD_s,borderRadius:3,borderSkipped:false}}]}},options:{{...baseOpts_s,plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{label:c=>` ${{c.raw.toLocaleString('pt-BR')}} cliques`}}}}}}}}}});
new Chart(document.getElementById('chartImpYTD-{sfx}'),{{type:'bar',data:{{labels:mesesYTD_s,datasets:[{{data:{J(ser(BASE['impressoes'], 'imp'))},backgroundColor:colsYTD_s,borderRadius:3,borderSkipped:false}}]}},options:{{...baseOpts_s,plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{label:c=>` ${{c.raw.toLocaleString('pt-BR')}}`}}}}}}}}}});
new Chart(document.getElementById('chartRevYTD-{sfx}'),{{type:'bar',data:{{labels:mesesYTD_s,datasets:[{{data:{J(ser(BASE['receita'], 'rev'))},backgroundColor:colsYTD_s,borderRadius:3,borderSkipped:false}}]}},options:{{...baseOpts_s,plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{label:c=>` R$ ${{c.raw.toLocaleString('pt-BR')}}`}}}}}}}}}});
new Chart(document.getElementById('chartOrdYTD-{sfx}'),{{type:'bar',data:{{labels:mesesYTD_s,datasets:[{{data:{J(ser(BASE['pedidos'], 'orders'))},backgroundColor:colsYTD_s,borderRadius:3,borderSkipped:false}}]}},options:{{...baseOpts_s,plugins:{{legend:{{display:false}},tooltip:{{callbacks:{{label:c=>` ${{c.raw}} pedidos`}}}}}}}}}});
const revPrev_s={J(P['receita_diaria'])};
const revCur_s={J(D['receita_diaria'])};
new Chart(document.getElementById('chartRevDaily-{sfx}'),{{type:'line',data:{{labels:dias31_s,datasets:[
  {{label:'{pab}',data:pad_s(revPrev_s,31),borderColor:C_PREV_S,backgroundColor:C_PREV_LS,tension:.3,pointRadius:0,borderWidth:2,fill:true}},
  {{label:'{ab}',data:pad_s(revCur_s,31),borderColor:C_CUR_S,backgroundColor:C_CUR_LS,tension:.3,pointRadius:0,borderWidth:2,fill:true}}
]}},options:{{...baseOpts_s,plugins:{{legend:{{display:true,labels:{{color:'#555',boxWidth:10,font:{{size:10,family:'Montserrat'}}}}}},tooltip:{{callbacks:{{label:c=>` R$ ${{(c.raw||0).toLocaleString('pt-BR')}}`}}}}}}}}}});

}})();
'''
    # --- aplica no index.html
    s = open(a.index, encoding='utf-8').read()
    assert f'id="tab-{sfx}"' not in s, f'a aba {sfx} já existe'
    btn_ant = re.search(r'<button class="tab-btn active" id="btn-(\w+)"', s)
    s = s.replace('<button class="tab-btn active"', '<button class="tab-btn"', 1)
    s = s.replace('<div class="tabs-nav">\n', f'<div class="tabs-nav">\n  <button class="tab-btn active" id="btn-{sfx}" onclick="showTab(\'{sfx}\')">{nome} {ano}</button>\n', 1)
    s = s.replace('class="tab-content active"', 'class="tab-content"')
    i = s.index('<div id="tab-')
    s = s[:i] + html + s[i:]
    j = s.index('\n(function(){', s.index('function showTab'))
    s = s[:j + 1] + js + s[j + 1:]
    open(a.out or a.index, 'w', encoding='utf-8').write(s)
    print(f'aba {sfx} gerada | cliques {M["cliques"]} imp {M["imp"]} ctr {M["ctr"]:.3f} pos {M["pos"]:.2f} sess {M["sess"]} rev {M["rev"]:.2f} ped {M["orders"]}')


if __name__ == '__main__':
    main()
