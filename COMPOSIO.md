# Configuração do Composio — como puxar os dados deste projeto

Documento de referência para qualquer chat aberto a partir deste repositório. O `CLAUDE.md` aponta para cá.
Objetivo: coletar **Google Search Console + GA4 (tráfego orgânico)** via Composio e manter `dados/` atualizado.

## 1. Key correta

| Item | Valor |
|---|---|
| Variável | `COMPOSIO_API_KEY` |
| Tipo | `ak_...` — Composio **Platform** → API Keys |
| Header | `x-api-key: <key>` |
| Permissão obrigatória | `tool_execution` com acesso **write** |
| Não usar | `ck_...` (consumer key do Composio For You): outro produto, não funciona aqui |

Erros comuns:
- `401 Invalid API key`: key errada, com erro de digitação ou revogada.
- `403 APIKey_InsufficientPermissions ... tool_execution`: a key lista contas, mas não executa ferramentas. Falta liberar a permissão no dashboard (ou criar uma key nova com ela).
- Em ambos os casos: peça ao usuário uma key nova e pare. Não tente contornar.

Onde guardar a key:
- **Só no ambiente**, como variável `COMPOSIO_API_KEY`. No Claude Code na web: menu do ambiente cloud → Edit → variável de ambiente/API credentials. Vale a partir de uma sessão nova. Local: arquivo `.env` (já ignorado pelo git; modelo em `.env.example`).
- **Nunca** colocar a key em arquivo versionado, commit, PR, log ou mensagem.
- **Nunca** pedir ao usuário que cole a key no chat. Se ele colar, use só naquela tarefa e recomende trocar a key depois.

## 2. Comportamento esperado em todo chat novo

1. Veja se `COMPOSIO_API_KEY` existe no ambiente (sem imprimir o valor).
2. Se existir, **colete os dados**: rode `python3 scripts/composio_coletar.py AAAA-MM` para cada mês fechado que não tenha arquivo em `dados/` ou cujo arquivo esteja com `"completo": false`. Mês fechado = qualquer mês anterior ao atual; o primeiro mês de `dados/` é `2026-08`.
3. Se não existir, diga ao usuário qual é a key correta (seção 1) e siga o que não depende dela. Não invente números.
4. Diga ao usuário, em uma linha, o que foi coletado e se algum mês ainda está parcial.
5. Coletar é só leitura. **Alterar `index.html`, abrir PR ou mesclar só quando o usuário pedir.**

## 3. Como coletar

```bash
export COMPOSIO_API_KEY=ak_...                                # normalmente já vem do ambiente
python3 scripts/composio_coletar.py 2026-10                   # GSC data_state=final (padrão)
python3 scripts/composio_coletar.py 2026-10 --data-state all  # inclui os últimos dias (preliminares)
```

O script descobre sozinho as contas ativas (`google_search_console` e `google_analytics`) com `GET /connected_accounts`, executa as ferramentas e grava `dados/AAAA-MM.json`. Usa só a biblioteca padrão do Python.

Chamada direta (se precisar sem o script):
- Base: `https://backend.composio.dev/api/v3.1`
- Contas: `GET /connected_accounts?limit=100`
- Executar: `POST /tools/execute/<SLUG>` com `{"connected_account_id": "...", "user_id": "...", "arguments": {...}}`
- Slugs: `GOOGLE_SEARCH_CONSOLE_SEARCH_ANALYTICS_QUERY` e `GOOGLE_ANALYTICS_RUN_REPORT`. Não invente slugs; descubra com `GET /tools?toolkit_slug=<toolkit>`.

## 4. Definições validadas

Conferidas contra o relatório publicado de Agosto/2026 (9.571 cliques, 1.689.302 impressões, 11.994 sessões, 9.806 usuários, R$34.379, 64 pedidos, 457 add-to-carts).

**Search Console** — site `https://www.ultramaquinas.com.br/` (variável opcional `GSC_SITE_URL`)
- Cliques e impressões: soma das linhas com dimensão `date`. CTR = cliques ÷ impressões.
- Posição média: **média ponderada por impressões**.
- Keywords: dimensão `query`, ordenadas por cliques. Páginas: dimensão `page`.
- `data_state` padrão (`final`) atrasa 2–3 dias; o último dia do mês pode faltar. `all` traz o dia preliminar. Quando usar dado preliminar, deixe isso explícito no relatório e reconfira depois.

**GA4** — property `326709572` (variável opcional `GA4_PROPERTY_ID`)
- Filtro: `sessionDefaultChannelGroup` igual a `Organic Search`.
- Métricas: `sessions`, `totalUsers`, `purchaseRevenue` (receita), `transactions` (pedidos), `addToCarts`.
- Ticket médio = receita ÷ pedidos. Taxa de conversão = pedidos ÷ sessões.

**Acumulado (YTD)**
- A barra "Jan/Fev*" do relatório entra duas vezes na soma. Base Jan–Ago/2026: cliques 80.138, impressões 13.781.942, receita R$252.866, pedidos 640, sessões 93.539.
- Mês novo: YTD = YTD anterior + valores do mês. Média mensal = YTD ÷ número de meses.

## 5. O que há em `dados/`

Cada `dados/AAAA-MM.json` traz: totais GSC e GA4 orgânico, cliques e receita por dia, top 50 keywords e top 50 páginas, mais os campos de controle `data_state_gsc`, `dias_gsc` e `completo`.

- `2026-08.json`: completo.
- `2026-09.json`: preliminar (GSC ainda sem o dia 30 como final). Será finalizado pela rotina do dia 05 (abaixo).

## Rotina mensal

Todo dia **05, às 9h48 (Brasília)** roda uma rotina que coleta o mês fechado, gera a aba no `index.html`, valida no navegador e **mescla na `main`** (autorizado pelo usuário). Em 05/10/2026 ela finaliza o PR #2 (Setembro) com os dados finais. Se o GSC ainda não tiver fechado o último dia, ela não publica e repete a checagem em 24h (até 3 vezes). **Não altere esse agendamento sem o usuário pedir.**

## 6. Relatório (`index.html`)

Uma aba por mês, a mais recente primeiro e ativa; ids com sufixo do mês (`tab-set`, `chartClicksDaily-set`...). Para criar a aba de um mês novo: copiar a estrutura da aba anterior, adicionar o botão em `tabs-nav`, o ponto novo nos gráficos YTD e um IIFE novo de gráficos (variáveis locais ao IIFE). Texto de insight factual, a partir dos números, sem adjetivos de intensidade. Entrega por branch + PR em draft; o preview da Vercel valida.
