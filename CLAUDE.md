# Ultramáquinas — Relatório SEO (contexto para o Claude)

Site: `index.html` publicado na Vercel (projeto `relatorio-seo-ultramaquinas`, deploy a partir da `main`; cada PR gera preview).
Uma aba por mês (`tab-set`, `tab-ago`, `tab-jul`, `tab-jun`), mais recente primeiro e ativa. Cada aba tem: resumo (KPIs + tabela vs mês anterior),
performance (cliques diários, CTR, posição), acumulado YTD, top 20 keywords, top 15 páginas e receita orgânica.
Fontes: Google Search Console + GA4 (tráfego "Organic Search"), coletados via **Composio**.

## Composio — qual key usar (leia antes de qualquer coleta)

- **Use a `COMPOSIO_API_KEY` do tipo `ak_...`** (Composio **Platform** → API Keys), enviada no header `x-api-key`.
- A key precisa ter a permissão **`tool_execution` com acesso `write`**. Sem ela, listar contas funciona, mas executar ferramentas retorna `403 APIKey_InsufficientPermissions`.
- **Não use a `ck_...`** (consumer key do Composio For You): é outro produto, não é intercambiável e não funciona neste fluxo.
- Erros: `401 Invalid API key` = key errada/revogada; `403 ... tool_execution` = falta permissão. Em ambos, peça uma nova key ao usuário.
- **A key fica só no ambiente**, como variável `COMPOSIO_API_KEY` (cloud: menu do ambiente → Edit → API credentials/variável de ambiente; local: `.env`, que está no `.gitignore`). Ela só vale em sessões novas.
- **Nunca** grave a key em arquivo versionado, commit, PR, log ou mensagem, e nunca peça ao usuário para colá-la no chat. Se ele colar uma key no chat, use-a só naquela tarefa e recomende trocar/revogar.
- Endpoint: `https://backend.composio.dev/api/v3.1`. Ferramentas: `POST /tools/execute/<SLUG>` com `connected_account_id`, `user_id`, `arguments`.
  As contas ativas (`google_search_console`, `google_analytics`) são descobertas por `GET /connected_accounts` — não fixe IDs.
- Slugs usados: `GOOGLE_SEARCH_CONSOLE_SEARCH_ANALYTICS_QUERY`, `GOOGLE_ANALYTICS_RUN_REPORT`. Não invente slugs; descubra com `GET /tools?toolkit_slug=...`.
- Skill de referência do Composio: `.agents/skills/composio/SKILL.md`.

## Como coletar

```bash
export COMPOSIO_API_KEY=ak_...                               # já definida no ambiente, normalmente
python3 scripts/composio_coletar.py 2026-10                  # GSC com data_state=final (padrão)
python3 scripts/composio_coletar.py 2026-10 --data-state all # inclui dias recentes (preliminares)
```

Grava `dados/AAAA-MM.json` (totais GSC/GA4, cliques e receita diários, top 50 keywords e páginas). Só biblioteca padrão.

### Definições validadas (batem com o relatório publicado de Agosto: 9.571 cliques, 11.994 sessões, R$34.379, 64 pedidos)
- GSC site `https://www.ultramaquinas.com.br/`. Cliques/impressões = soma das linhas por `date`. CTR = cliques/impressões. **Posição = média ponderada por impressões**.
- GA4 property `326709572`, filtro `sessionDefaultChannelGroup == "Organic Search"`. Métricas: `sessions`, `totalUsers`, `purchaseRevenue` (receita), `transactions` (pedidos), `addToCarts`.
  Ticket médio = receita/pedidos. Conversão = pedidos/sessões.
- **GSC: `data_state` padrão (`final`) atrasa ~2–3 dias**; o último dia do mês pode faltar. `all` traz o dado preliminar. Marque no relatório quando usar dado preliminar e reconfira depois.
- YTD: o "Jan/Fev*" do relatório é uma barra única que entra **duas vezes** na soma (ver cards YTD de Agosto: cliques 80.138, impressões 13.781.942, receita R$252.866, pedidos 640, sessões 93.539). Para um novo mês: YTD = YTD do mês anterior + valores do mês; média mensal = YTD ÷ nº de meses.

## Dados atualizados (regra para todo chat)

`dados/` é a fonte coletada via Composio. **Ao começar um chat sobre este repo:**
1. Veja o mês mais recente em `dados/` e compare com a data de hoje. Se existir mês fechado sem arquivo, ou arquivo com `completo: false` (preliminar) cujo mês já pode estar final, avise o usuário no início.
2. Havendo `COMPOSIO_API_KEY` no ambiente, atualize `dados/` rodando o script (coleta é só leitura). Sem a key, diga qual é a correta (seção acima).
3. Só altere `index.html`, abra PR ou faça merge quando o usuário pedir. Ao criar a aba de um mês: copie a estrutura da aba anterior, sufixo de ids `-set`/`-ago`…, adicione o botão no `tabs-nav`, ponto novo no YTD e um IIFE novo de gráficos (variáveis locais ao IIFE).
4. Texto de insight: factual, a partir dos números, sem adjetivos de intensidade. Entrega por branch + PR em draft; o preview da Vercel valida.

Arquivos: `dados/2026-08.json` (completo), `dados/2026-09.json` (preliminar até o GSC fechar 30/09; a revisão está agendada para 04/10/2026).
