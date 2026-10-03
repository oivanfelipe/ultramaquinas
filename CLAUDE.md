# Ultramáquinas — Relatório SEO (contexto para o Claude)

Site: `index.html` publicado na Vercel (projeto `relatorio-seo-ultramaquinas`, deploy a partir da `main`; cada PR gera preview).
Uma aba por mês (`tab-set`, `tab-ago`, `tab-jul`, `tab-jun`), a mais recente primeiro e ativa. Cada aba tem: resumo (KPIs + tabela vs mês anterior), performance (cliques diários, CTR, posição), acumulado YTD, top 20 keywords, top 15 páginas e receita orgânica.
Fontes: Google Search Console + GA4 (tráfego "Organic Search"), coletados via **Composio**.

## Dados via Composio — leia `COMPOSIO.md` antes de qualquer coleta

Em todo chat novo neste repositório, siga o `COMPOSIO.md`: ele diz qual key usar, como coletar os dados com `scripts/composio_coletar.py`, as definições de métricas já validadas e o que está em `dados/`.

Resumo:
- Key correta: **`COMPOSIO_API_KEY` tipo `ak_...`** (Platform) com permissão **`tool_execution` = write**. Não usar a `ck_...`.
- A key fica só no ambiente. Nunca em arquivo versionado, commit, log ou mensagem; nunca peça para o usuário colá-la no chat.
- Com a key no ambiente, colete os meses fechados que faltam em `dados/`. Sem ela, diga qual é a correta e não invente números.
- Coletar é só leitura. Alterar `index.html`, abrir PR ou mesclar só quando o usuário pedir.
- Há uma rotina mensal no dia 05 que atualiza o relatório e mescla na `main` (detalhes no `COMPOSIO.md`). Não altere esse agendamento.
