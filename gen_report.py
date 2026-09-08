import re

# ── Read existing reports ──────────────────────────────────────────────────
with open('/root/.claude/uploads/c3171493-9162-5bf7-ab45-8949acc4770e/f34e2088-relatorioseoultramaquinasjulho2026.html') as f:
    jul_html = f.read()
with open('/root/.claude/uploads/c3171493-9162-5bf7-ab45-8949acc4770e/88f2a1d6-relatorioseoultramaquinasjunho2026.html') as f:
    jun_html = f.read()

shared_style = re.search(r'<style[^>]*>(.*?)</style>', jul_html, re.DOTALL).group(1)

jul_body_raw = re.search(r'<body[^>]*>(.*)</body>', jul_html, re.DOTALL).group(1).strip()
jul_script_raw = re.search(r'<script(?!\s+src)[^>]*>(.*?)</script>', jul_html, re.DOTALL).group(1)
# Strip embedded <script> blocks from body — scripts are re-added separately after suffix renaming
jul_body = re.sub(r'<script[^>]*>.*?</script>', '', jul_body_raw, flags=re.DOTALL).strip()

jun_body_raw = re.search(r'<body[^>]*>(.*)</body>', jun_html, re.DOTALL).group(1).strip()
jun_script_raw = re.search(r'<script(?!\s+src)[^>]*>(.*?)</script>', jun_html, re.DOTALL).group(1)
jun_body = re.sub(r'<script[^>]*>.*?</script>', '', jun_body_raw, flags=re.DOTALL).strip()

def suffix_ids(html, js, suffix):
    canvas_ids = re.findall(r'<canvas[^>]+id=["\']([^"\']+)["\']', html)
    nh, nj = html, js
    for cid in set(canvas_ids):
        nh = nh.replace(f'id="{cid}"', f'id="{cid}-{suffix}"')
        nh = nh.replace(f"id='{cid}'", f"id='{cid}-{suffix}'")
        nj = nj.replace(f"'{cid}'", f"'{cid}-{suffix}'")
        nj = nj.replace(f'"{cid}"', f'"{cid}-{suffix}"')
    return nh, nj

jul_body_r, jul_script_r = suffix_ids(jul_body, jul_script_raw, 'jul')
jun_body_r, jun_script_r = suffix_ids(jun_body, jun_script_raw, 'jun')

# ── August data ────────────────────────────────────────────────────────────
ago_cliques = 9571; ago_imp = 1689302; ago_ctr = 0.5666; ago_pos = 6.977
ago_sessoes = 11994; ago_usuarios = 9806; ago_pedidos = 64; ago_receita = 34379
ago_ticket = 537; ago_addcarts = 457

jul_cliques = 9339; jul_imp = 1357607; jul_ctr = 0.69; jul_pos = 7.18
jul_sessoes = 10882; jul_usuarios = 8659; jul_pedidos = 71; jul_receita = 19413; jul_ticket = 273

def fmt_br(n):
    return f'{int(n):,}'.replace(',', '.')

def pct(a, b):
    return (a - b) / b * 100

ytd_cliques_total = 80138
ytd_imp_total = 13781942
ytd_receita_total = 252866
ytd_pedidos_total = 640
ytd_sessoes_total = 93539
ytd_ticket_total = round(ytd_receita_total / ytd_pedidos_total)

ago_clicks_daily = [162,151,376,341,377,369,326,173,136,366,418,407,413,327,166,148,434,412,408,357,361,132,132,399,421,400,395,362,148,166,388]
jul_clicks_daily = [425,344,351,177,113,370,371,395,281,354,161,156,373,394,314,345,330,136,114,351,364,349,364,327,146,138,396,380,334,401,285]
ago_rev_daily = [3522.11,0,1595.86,125.26,2017.17,2124.10,0,1425.50,0,904.18,0,3757.95,270.29,63.18,0,0,2477.82,0,5032.13,296.00,950.47,0,0,6151.15,62.89,803.59,0,2042.37,0,0,757.12]
jul_rev_daily = [1394.75,360.51,459.42,0,0,0,669.46,2697.11,0,2181.9,0,0,317.9,848.97,32.25,268.01,889.72,114.61,165.19,110.66,503.57,638.41,1116.87,1376.68,0,66.07,1733.04,0,0,1034.53,2433.77]

ytd_cliques = [10957,11228,9719,9181,9186,9339,9571]
ytd_imp = [1941101,1960672,1624785,1647751,1619624,1357607,1689302]
ytd_receita = [35753,38074,35314,22926,31253,19413,34379]
ytd_pedidos = [100,68,99,55,83,71,64]

queries = [
    ('ultra maquinas',151,0.1016,1486,2.06),
    ('ultramaquinas',125,0.1724,725,2.16),
    ('ultra maquinas campinas',28,0.0632,443,2.75),
    ('ultra máquinas',23,0.1257,183,1.56),
    ('ultra máquinas aricanduva',21,0.0968,217,1.65),
    ('ultra maquinas comercial de ferramentas ltda',18,0.1682,107,5.12),
    ('chave l',13,0.0009,14193,1.04),
    ('digimess',12,0.0101,1187,7.43),
    ('hammer ferramentas',12,0.0736,163,5.91),
    ('hammer',11,0.0033,3361,8.98),
    ('lixadeira de madeira',11,0.0023,4790,4.71),
    ('ultramaquinas campinas',10,0.04,250,1.64),
    ('carrinho de carga dobrável',9,0.0031,2949,9.58),
    ('fercar',9,0.0118,763,7.43),
    ('preço',9,0.0216,416,9.07),
    ('ultra máquina',9,0.1607,56,1.96),
    ('product',8,0.0293,273,1.00),
    ('solplast',8,0.012,665,6.32),
    ('bateria parafusadeira skil 9 6v',7,0.0722,97,5.64),
    ('bucha furadeira bosch super hobby',7,0.2414,29,1.07),
]

pages = [
    ('/ (Home)',568,0.0421,13492,5.93),
    ('/pecas-de-reposicao/induzido',97,0.0132,7371,7.63),
    ('/nossaslojas',80,0.0126,6355,2.64),
    ('/produto/bateria-9-6v-parafusadeira-skil-2212…',61,0.0725,841,6.40),
    ('/ferramentas-eletricas/lixadeiras-p/madeira',56,0.0029,19422,8.63),
    ('/produto/macaco-hidraulico-jacare-3-5-ton…',43,0.0165,2605,4.53),
    ('/fabricante/hammer',42,0.0088,4761,8.82),
    ('/casa/carrinho-dobravel',38,0.0037,10184,8.63),
    ('/produto/defende-ela-spray-poly-defensor-50g…',38,0.0236,1608,6.79),
    ('/pecas-de-reposicao/pecas',34,0.0171,1993,8.96),
    ('/produto/nivel-de-aluminio-2-00m-magnetico-mtx…',33,0.0085,3864,4.07),
    ('/produto/esmerilhadeira-angular-4-1-2-gws-7-115…',31,0.011,2829,5.82),
    ('/produto/lavadora-de-alta-pressao-power-pro-2800…',31,0.0443,699,4.38),
    ('/pecas-de-reposicao/estator-e-bobina',28,0.011,2547,7.63),
    ('/pecas-de-reposicao/escova-de-carvao',26,0.0067,3854,9.39),
]

queries_rows = ''
for i,(kw,clk,ctr,imp,pos) in enumerate(queries,1):
    queries_rows += f'<tr><td>{i}</td><td>{kw}</td><td class="num">{clk}</td><td class="num">{fmt_br(imp)}</td><td class="num">{ctr*100:.2f}%</td><td class="num">{pos:.2f}</td></tr>\n'

pages_rows = ''
for i,(pg,clk,ctr,imp,pos) in enumerate(pages,1):
    pages_rows += f'<tr><td>{i}</td><td class="url">{pg}</td><td class="num">{clk}</td><td class="num">{fmt_br(imp)}</td><td class="num">{ctr*100:.2f}%</td><td class="num">{pos:.2f}</td></tr>\n'

ago_body = """
<div class="header">
  <div class="header-tag">// SEO Performance Report · Jan–Ago 2026</div>
  <h1>Ultramáquinas<br><span>Relatório SEO</span> — Agosto 2026</h1>
  <div class="header-meta">
    <div class="header-meta-item">Período atual <strong>01–31 Ago 2026</strong></div>
    <div class="header-meta-item">Comparativo <strong>Jul 2026</strong></div>
    <div class="header-meta-item">Acumulado <strong>Jan–Ago 2026</strong></div>
    <div class="header-meta-item">Domínio <strong>ultramaquinas.com.br</strong></div>
    <div class="header-meta-item">Gerado em <strong>07 Set 2026</strong></div>
  </div>
</div>

<nav class="nav">
  <a href="#resumo-ago">01 Resumo</a>
  <a href="#performance-ago">02 Performance</a>
  <a href="#ytd-ago">03 Acumulado YTD</a>
  <a href="#keywords-ago">04 Keywords</a>
  <a href="#paginas-ago">05 Páginas</a>
  <a href="#receita-ago">06 Receita</a>
</nav>

<div class="container">

<!-- 01 RESUMO -->
<section class="section" id="resumo-ago">
  <div class="section-label">01</div>
  <div class="section-title">Resumo <span>Executivo</span></div>
  <div class="scorecard-grid">
    <div class="scorecard up">
      <div class="scorecard-label">Cliques Orgânicos</div>
      <div class="scorecard-value">__AGO_CLIQUES__</div>
      <span class="scorecard-delta up">▲ +2,5% vs Jul</span>
      <div class="scorecard-prev">Jul: __JUL_CLIQUES__</div>
    </div>
    <div class="scorecard up">
      <div class="scorecard-label">Impressões Orgânicas</div>
      <div class="scorecard-value">__AGO_IMP__</div>
      <span class="scorecard-delta up">▲ +24,4% vs Jul</span>
      <div class="scorecard-prev">Jul: __JUL_IMP__</div>
    </div>
    <div class="scorecard down">
      <div class="scorecard-label">CTR Orgânico</div>
      <div class="scorecard-value">0,57%</div>
      <span class="scorecard-delta down">▼ -0,12 pp vs Jul</span>
      <div class="scorecard-prev">Jul: 0,69%</div>
    </div>
    <div class="scorecard up">
      <div class="scorecard-label">Posição Média</div>
      <div class="scorecard-value">6,98</div>
      <span class="scorecard-delta up">▲ +0,20 pos vs Jul</span>
      <div class="scorecard-prev">Jul: 7,18</div>
    </div>
    <div class="scorecard up">
      <div class="scorecard-label">Receita Orgânica</div>
      <div class="scorecard-value">R$__AGO_RECEITA__</div>
      <span class="scorecard-delta up">▲ +77,1% vs Jul</span>
      <div class="scorecard-prev">Jul: R$__JUL_RECEITA__</div>
    </div>
  </div>

  <div class="insight-box">
    <p>Agosto encerrou com crescimento em cliques (+2,5%), sessões (+10,2%) e receita orgânica (+77,1%), impulsionado pela recuperação das impressões (+24,4%) e melhora de 0,20 posições na posição média. A queda no volume de pedidos (-9,9%) foi compensada pelo salto no ticket médio (+96,7%, chegando a R$537), sinalizando conversão de transações de maior valor no canal orgânico.</p>
  </div>

  <div class="table-wrap">
    <table>
      <thead><tr><th>Métrica</th><th>Agosto 2026</th><th>Julho 2026</th><th>Ago vs Jul</th></tr></thead>
      <tbody>
        <tr><td>Cliques Orgânicos</td><td class="num">__AGO_CLIQUES__</td><td class="num">__JUL_CLIQUES__</td><td class="tag-up">▲ +2,5%</td></tr>
        <tr><td>Impressões Orgânicas</td><td class="num">__AGO_IMP__</td><td class="num">__JUL_IMP__</td><td class="tag-up">▲ +24,4%</td></tr>
        <tr><td>CTR Orgânico</td><td class="num">0,57%</td><td class="num">0,69%</td><td class="tag-down">▼ -0,12 pp</td></tr>
        <tr><td>Posição Média</td><td class="num">6,98</td><td class="num">7,18</td><td class="tag-up">▲ +0,20 pos</td></tr>
        <tr><td>Sessões Orgânicas</td><td class="num">__AGO_SESSOES__</td><td class="num">__JUL_SESSOES__</td><td class="tag-up">▲ +10,2%</td></tr>
        <tr><td>Usuários Orgânicos</td><td class="num">__AGO_USUARIOS__</td><td class="num">__JUL_USUARIOS__</td><td class="tag-up">▲ +13,2%</td></tr>
        <tr><td>Receita Orgânica</td><td class="num">R$__AGO_RECEITA__</td><td class="num">R$__JUL_RECEITA__</td><td class="tag-up">▲ +77,1%</td></tr>
        <tr><td>Pedidos Orgânicos</td><td class="num">__AGO_PEDIDOS__</td><td class="num">__JUL_PEDIDOS__</td><td class="tag-down">▼ -9,9%</td></tr>
        <tr><td>Ticket Médio</td><td class="num">R$__AGO_TICKET__</td><td class="num">R$__JUL_TICKET__</td><td class="tag-up">▲ +96,7%</td></tr>
      </tbody>
    </table>
  </div>
</section>

<!-- 02 PERFORMANCE -->
<section class="section" id="performance-ago">
  <div class="section-label">02</div>
  <div class="section-title">Performance <span>Orgânica</span></div>
  <div class="charts-row">
    <div class="chart-block" style="flex:2">
      <div class="chart-title">Cliques Diários — Jul vs Ago 2026</div>
      <canvas id="chartClicksDaily-ago" height="120"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">CTR Orgânico</div>
      <canvas id="chartCTR-ago" height="120"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">Posição Média</div>
      <canvas id="chartPosition-ago" height="120"></canvas>
    </div>
  </div>
</section>

<!-- 03 YTD -->
<section class="section" id="ytd-ago">
  <div class="section-label">03</div>
  <div class="section-title">Acumulado <span>Jan–Ago 2026</span></div>
  <div class="ytd-cards">
    <div class="ytd-card">
      <div class="ytd-card-label">Cliques Orgânicos YTD</div>
      <div class="ytd-card-value">__YTD_CLIQUES__</div>
      <div class="ytd-card-sub">Média mensal: __YTD_CLIQUES_MED__</div>
    </div>
    <div class="ytd-card">
      <div class="ytd-card-label">Impressões YTD</div>
      <div class="ytd-card-value">__YTD_IMP__</div>
      <div class="ytd-card-sub">Média mensal: __YTD_IMP_MED__</div>
    </div>
    <div class="ytd-card">
      <div class="ytd-card-label">Receita Orgânica YTD</div>
      <div class="ytd-card-value">R$__YTD_RECEITA__</div>
      <div class="ytd-card-sub">Média mensal: R$__YTD_RECEITA_MED__</div>
    </div>
    <div class="ytd-card">
      <div class="ytd-card-label">Pedidos Orgânicos YTD</div>
      <div class="ytd-card-value">__YTD_PEDIDOS__</div>
      <div class="ytd-card-sub">Média mensal: __YTD_PEDIDOS_MED__</div>
    </div>
    <div class="ytd-card">
      <div class="ytd-card-label">Sessões Orgânicas YTD</div>
      <div class="ytd-card-value">__YTD_SESSOES__</div>
      <div class="ytd-card-sub">Média mensal: __YTD_SESSOES_MED__</div>
    </div>
    <div class="ytd-card">
      <div class="ytd-card-label">Ticket Médio YTD</div>
      <div class="ytd-card-value">R$__YTD_TICKET__</div>
      <div class="ytd-card-sub">Total: __YTD_PEDIDOS__ pedidos</div>
    </div>
  </div>
  <div class="charts-row">
    <div class="chart-block">
      <div class="chart-title">Cliques por Mês (YTD)</div>
      <canvas id="chartClicksYTD-ago" height="130"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">Impressões por Mês (YTD)</div>
      <canvas id="chartImpYTD-ago" height="130"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">Receita por Mês (YTD)</div>
      <canvas id="chartRevYTD-ago" height="130"></canvas>
    </div>
    <div class="chart-block">
      <div class="chart-title">Pedidos por Mês (YTD)</div>
      <canvas id="chartOrdYTD-ago" height="130"></canvas>
    </div>
  </div>
</section>

<!-- 04 KEYWORDS -->
<section class="section" id="keywords-ago">
  <div class="section-label">04</div>
  <div class="section-title">Análise de <span>Palavras-chave</span></div>
  <p class="section-desc">Top 20 keywords por cliques orgânicos — Agosto 2026 · Google Search Console</p>
  <div class="table-wrap">
    <table>
      <thead><tr><th>#</th><th>Keyword</th><th>Cliques</th><th>Impressões</th><th>CTR</th><th>Posição</th></tr></thead>
      <tbody>
__QUERIES_ROWS__
      </tbody>
    </table>
  </div>
</section>

<!-- 05 PÁGINAS -->
<section class="section" id="paginas-ago">
  <div class="section-label">05</div>
  <div class="section-title">Páginas com Melhor <span>Desempenho</span></div>
  <p class="section-desc">Top 15 páginas por cliques orgânicos — Agosto 2026 · Google Search Console</p>
  <div class="table-wrap">
    <table>
      <thead><tr><th>#</th><th>Página</th><th>Cliques</th><th>Impressões</th><th>CTR</th><th>Posição</th></tr></thead>
      <tbody>
__PAGES_ROWS__
      </tbody>
    </table>
  </div>
</section>

<!-- 06 RECEITA -->
<section class="section" id="receita-ago">
  <div class="section-label">06</div>
  <div class="section-title">Faturamento <span>Orgânico</span></div>
  <div class="scorecard-grid">
    <div class="scorecard up">
      <div class="scorecard-label">Receita Orgânica</div>
      <div class="scorecard-value">R$__AGO_RECEITA__</div>
      <span class="scorecard-delta up">▲ +77,1% vs Jul</span>
      <div class="scorecard-prev">Jul: R$__JUL_RECEITA__</div>
    </div>
    <div class="scorecard down">
      <div class="scorecard-label">Pedidos Orgânicos</div>
      <div class="scorecard-value">__AGO_PEDIDOS__</div>
      <span class="scorecard-delta down">▼ -9,9% vs Jul</span>
      <div class="scorecard-prev">Jul: __JUL_PEDIDOS__</div>
    </div>
    <div class="scorecard up">
      <div class="scorecard-label">Ticket Médio</div>
      <div class="scorecard-value">R$__AGO_TICKET__</div>
      <span class="scorecard-delta up">▲ +96,7% vs Jul</span>
      <div class="scorecard-prev">Jul: R$__JUL_TICKET__</div>
    </div>
    <div class="scorecard up">
      <div class="scorecard-label">Add-to-Carts</div>
      <div class="scorecard-value">__AGO_ADDCARTS__</div>
      <span class="scorecard-delta up">▲ +8,8% vs Jul</span>
      <div class="scorecard-prev">Jul: 420</div>
    </div>
    <div class="scorecard up">
      <div class="scorecard-label">Sessões Orgânicas</div>
      <div class="scorecard-value">__AGO_SESSOES__</div>
      <span class="scorecard-delta up">▲ +10,2% vs Jul</span>
      <div class="scorecard-prev">Jul: __JUL_SESSOES__</div>
    </div>
    <div class="scorecard up">
      <div class="scorecard-label">Taxa de Conversão</div>
      <div class="scorecard-value">0,53%</div>
      <span class="scorecard-delta down">▼ -0,12 pp vs Jul</span>
      <div class="scorecard-prev">Jul: 0,65%</div>
    </div>
  </div>
  <div class="chart-wide">
    <div class="chart-title">Receita Orgânica Diária — Jul vs Ago 2026</div>
    <canvas id="chartRevDaily-ago"></canvas>
  </div>
</section>

</div>

<div class="footer">
  <span>Dados: Google Search Console · Google Analytics 4 (Tráfego Orgânico)</span>
  <span>Ultramáquinas · Relatório SEO Agosto 2026 · Gerado em 07/09/2026</span>
</div>
"""

# Replace placeholders
ago_body = (ago_body
    .replace('__AGO_CLIQUES__', fmt_br(ago_cliques))
    .replace('__JUL_CLIQUES__', fmt_br(jul_cliques))
    .replace('__AGO_IMP__', fmt_br(ago_imp))
    .replace('__JUL_IMP__', fmt_br(jul_imp))
    .replace('__AGO_RECEITA__', fmt_br(ago_receita))
    .replace('__JUL_RECEITA__', fmt_br(jul_receita))
    .replace('__AGO_SESSOES__', fmt_br(ago_sessoes))
    .replace('__JUL_SESSOES__', fmt_br(jul_sessoes))
    .replace('__AGO_USUARIOS__', fmt_br(ago_usuarios))
    .replace('__JUL_USUARIOS__', fmt_br(jul_usuarios))
    .replace('__AGO_PEDIDOS__', str(ago_pedidos))
    .replace('__JUL_PEDIDOS__', str(jul_pedidos))
    .replace('__AGO_TICKET__', fmt_br(ago_ticket))
    .replace('__JUL_TICKET__', fmt_br(jul_ticket))
    .replace('__AGO_ADDCARTS__', fmt_br(ago_addcarts))
    .replace('__YTD_CLIQUES__', fmt_br(ytd_cliques_total))
    .replace('__YTD_CLIQUES_MED__', fmt_br(ytd_cliques_total // 8))
    .replace('__YTD_IMP__', fmt_br(ytd_imp_total))
    .replace('__YTD_IMP_MED__', fmt_br(ytd_imp_total // 8))
    .replace('__YTD_RECEITA__', fmt_br(ytd_receita_total))
    .replace('__YTD_RECEITA_MED__', fmt_br(ytd_receita_total // 8))
    .replace('__YTD_PEDIDOS__', str(ytd_pedidos_total))
    .replace('__YTD_PEDIDOS_MED__', str(ytd_pedidos_total // 8))
    .replace('__YTD_SESSOES__', fmt_br(ytd_sessoes_total))
    .replace('__YTD_SESSOES_MED__', fmt_br(ytd_sessoes_total // 8))
    .replace('__YTD_TICKET__', fmt_br(ytd_ticket_total))
    .replace('__QUERIES_ROWS__', queries_rows)
    .replace('__PAGES_ROWS__', pages_rows)
)

# ── August JS (no f-string, use concatenation) ────────────────────────────
ago_script = (
    "const grid_ago='rgba(0,0,0,0.06)';\n"
    "const baseOpts_ago={responsive:true,maintainAspectRatio:true,plugins:{legend:{display:false}},scales:{x:{grid:{color:grid_ago},ticks:{color:'#aaa',maxTicksLimit:8}},y:{grid:{color:grid_ago},ticks:{color:'#aaa',maxTicksLimit:5}}}};\n"
    "const C_JUL_A='rgba(27,127,62,0.85)',C_AGO_A='rgba(204,0,0,0.85)';\n"
    "const C_JUL_LA='rgba(27,127,62,0.12)',C_AGO_LA='rgba(204,0,0,0.12)';\n"
    "const cliqJul_a=" + str(jul_clicks_daily) + ";\n"
    "const cliqAgo_a=" + str(ago_clicks_daily) + ";\n"
    "const dias31_a=Array.from({length:31},(_,i)=>i+1);\n"
    "const pad_a=(arr,n)=>[...arr,...Array(Math.max(0,n-arr.length)).fill(null)];\n"
    "new Chart(document.getElementById('chartClicksDaily-ago'),{type:'line',data:{labels:dias31_a,datasets:[\n"
    "  {label:'Jul',data:pad_a(cliqJul_a,31),borderColor:C_JUL_A,backgroundColor:C_JUL_LA,tension:.3,pointRadius:0,borderWidth:2,fill:false},\n"
    "  {label:'Ago',data:pad_a(cliqAgo_a,31),borderColor:C_AGO_A,backgroundColor:C_AGO_LA,tension:.3,pointRadius:0,borderWidth:2,fill:false}\n"
    "]},options:{...baseOpts_ago,plugins:{legend:{display:true,labels:{color:'#555',boxWidth:10,font:{size:10,family:'Montserrat'}}}}}});\n"
    "new Chart(document.getElementById('chartCTR-ago'),{type:'bar',data:{labels:['Jul 2026','Ago 2026'],datasets:[{data:[0.69,0.57],backgroundColor:[C_JUL_A,C_AGO_A],borderRadius:3,borderSkipped:false}]},options:{...baseOpts_ago,plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>` ${c.raw.toFixed(2)}%`}}},scales:{...baseOpts_ago.scales,y:{...baseOpts_ago.scales.y,min:0.45,max:0.80,ticks:{callback:v=>v.toFixed(2)+'%',color:'#555',maxTicksLimit:5}}}}});\n"
    "new Chart(document.getElementById('chartPosition-ago'),{type:'bar',data:{labels:['Jul 2026','Ago 2026'],datasets:[{data:[7.18,6.98],backgroundColor:[C_JUL_A,C_AGO_A],borderRadius:3,borderSkipped:false}]},options:{...baseOpts_ago,plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>` ${c.raw.toFixed(2)}`}}},scales:{...baseOpts_ago.scales,y:{...baseOpts_ago.scales.y,min:6.5,max:7.5,ticks:{callback:v=>v.toFixed(2),color:'#555',maxTicksLimit:5}}}}});\n"
    "const mesesYTD_a=['Jan/Fev*','Mar','Abr','Mai','Jun','Jul','Ago'];\n"
    "const colsYTD_a=['rgba(180,180,180,0.85)','rgba(130,130,130,0.85)','rgba(80,80,80,0.85)','rgba(204,0,0,0.70)','rgba(26,26,26,0.85)','rgba(27,127,62,0.85)','rgba(204,0,0,0.85)'];\n"
    "new Chart(document.getElementById('chartClicksYTD-ago'),{type:'bar',data:{labels:mesesYTD_a,datasets:[{data:" + str(ytd_cliques) + ",backgroundColor:colsYTD_a,borderRadius:3,borderSkipped:false}]},options:{...baseOpts_ago,plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>` ${c.raw.toLocaleString('pt-BR')} cliques`}}}}});\n"
    "new Chart(document.getElementById('chartImpYTD-ago'),{type:'bar',data:{labels:mesesYTD_a,datasets:[{data:" + str(ytd_imp) + ",backgroundColor:colsYTD_a,borderRadius:3,borderSkipped:false}]},options:{...baseOpts_ago,plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>` ${c.raw.toLocaleString('pt-BR')}`}}}}});\n"
    "new Chart(document.getElementById('chartRevYTD-ago'),{type:'bar',data:{labels:mesesYTD_a,datasets:[{data:" + str(ytd_receita) + ",backgroundColor:colsYTD_a,borderRadius:3,borderSkipped:false}]},options:{...baseOpts_ago,plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>` R$ ${c.raw.toLocaleString('pt-BR')}`}}}}});\n"
    "new Chart(document.getElementById('chartOrdYTD-ago'),{type:'bar',data:{labels:mesesYTD_a,datasets:[{data:" + str(ytd_pedidos) + ",backgroundColor:colsYTD_a,borderRadius:3,borderSkipped:false}]},options:{...baseOpts_ago,plugins:{legend:{display:false},tooltip:{callbacks:{label:c=>` ${c.raw} pedidos`}}}}});\n"
    "const revJul_a=" + str(jul_rev_daily) + ";\n"
    "const revAgo_a=" + str(ago_rev_daily) + ";\n"
    "new Chart(document.getElementById('chartRevDaily-ago'),{type:'line',data:{labels:dias31_a,datasets:[\n"
    "  {label:'Jul',data:pad_a(revJul_a,31),borderColor:C_JUL_A,backgroundColor:C_JUL_LA,tension:.3,pointRadius:0,borderWidth:2,fill:true},\n"
    "  {label:'Ago',data:pad_a(revAgo_a,31),borderColor:C_AGO_A,backgroundColor:C_AGO_LA,tension:.3,pointRadius:0,borderWidth:2,fill:true}\n"
    "]},options:{...baseOpts_ago,plugins:{legend:{display:true,labels:{color:'#555',boxWidth:10,font:{size:10,family:'Montserrat'}}},tooltip:{callbacks:{label:c=>` R$ ${(c.raw||0).toLocaleString('pt-BR')}`}}}}});\n"
)

tab_css = """
/* ── Tab navigation ── */
.tabs-nav {
  position: sticky;
  top: 0;
  z-index: 100;
  background: #fff;
  border-bottom: 2px solid #f0f0f0;
  display: flex;
  gap: 0;
  padding: 0 32px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}
.tab-btn {
  background: none;
  border: none;
  border-bottom: 3px solid transparent;
  cursor: pointer;
  font-family: 'Montserrat', sans-serif;
  font-size: 13px;
  font-weight: 600;
  color: #888;
  padding: 14px 24px;
  margin-bottom: -2px;
  transition: color 0.2s, border-color 0.2s;
  letter-spacing: 0.02em;
}
.tab-btn:hover { color: #333; }
.tab-btn.active { color: #CC0000; border-bottom-color: #CC0000; }
.tab-content { display: none; }
.tab-content.active { display: block; }
td.url { font-size: 11px; font-family: monospace; max-width: 280px; word-break: break-all; }
.kpi-row { display: flex; flex-wrap: wrap; gap: 12px; margin-bottom: 24px; }
.kpi-box { background: #f8f8f8; border-radius: 8px; padding: 16px 20px; min-width: 130px; flex: 1; }
.kpi-label { font-size: 11px; color: #888; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 6px; }
.kpi-value { font-size: 22px; font-weight: 800; color: #1a1a1a; }
.section-desc { color: #888; font-size: 13px; margin: -8px 0 16px; }
"""

tab_js = """
function showTab(t) {
  document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
  document.getElementById('tab-' + t).classList.add('active');
  document.getElementById('btn-' + t).classList.add('active');
  // Trigger Chart.js resize for charts in the newly visible tab
  window.dispatchEvent(new Event('resize'));
}
"""

html_parts = [
    '<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n',
    '  <meta charset="UTF-8">\n',
    '  <meta name="viewport" content="width=device-width,initial-scale=1">\n',
    '  <title>Relatório SEO · Ultramáquinas 2026</title>\n',
    '  <link rel="preconnect" href="https://fonts.googleapis.com">\n',
    '  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&family=Inter:wght@400;500&display=swap" rel="stylesheet">\n',
    '  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>\n',
    '  <style>\n', shared_style, '\n', tab_css, '\n  </style>\n',
    '</head>\n<body>\n\n',
    '<div class="tabs-nav">\n',
    '  <button class="tab-btn active" id="btn-ago" onclick="showTab(\'ago\')">Agosto 2026</button>\n',
    '  <button class="tab-btn" id="btn-jul" onclick="showTab(\'jul\')">Julho 2026</button>\n',
    '  <button class="tab-btn" id="btn-jun" onclick="showTab(\'jun\')">Junho 2026</button>\n',
    '</div>\n\n',
    '<div id="tab-ago" class="tab-content active">\n', ago_body, '\n</div>\n\n',
    '<div id="tab-jul" class="tab-content">\n', jul_body_r, '\n</div>\n\n',
    '<div id="tab-jun" class="tab-content">\n', jun_body_r, '\n</div>\n\n',
    '<script>\n', tab_js, '\n',
    '(function(){\n', ago_script, '\n})();\n',
    '(function(){\n', jul_script_r, '\n})();\n',
    '(function(){\n', jun_script_r, '\n})();\n',
    '</script>\n</body>\n</html>\n',
]

html = ''.join(html_parts)

output_path = '/home/user/ultramaquinas/index.html'
with open(output_path, 'w') as f:
    f.write(html)

print(f"Written: {len(html):,} bytes to {output_path}")
