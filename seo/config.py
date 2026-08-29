"""
Configurações do sistema SEO — Ultra Máquinas

Chaves de API: defina como variáveis de ambiente antes de rodar.
Exemplo (.env ou export):
  export GOOGLE_API_KEY="..."
  export GOOGLE_ANALYTICS_API_KEY="..."
  export ANTHROPIC_API_KEY="..."
"""

import os

# ─── Google APIs ────────────────────────────────────────────────────────────────
# Custom Search API (para SERP analysis — etapa 3 do pipeline)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")

# Google Analytics Data API key
GOOGLE_ANALYTICS_API_KEY = os.getenv("GOOGLE_ANALYTICS_API_KEY", "")

# Google Analytics 4 Property ID (obter em: analytics.google.com → Admin → Property → Property ID)
GOOGLE_ANALYTICS_PROPERTY_ID = os.getenv("GOOGLE_ANALYTICS_PROPERTY_ID", "")  # ex: "properties/123456789"

# Google Custom Search Engine ID (obter em: https://cse.google.com)
# Configurar para pesquisar apenas resultados orgânicos do Google.com.br
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID", "")  # TODO: criar CSE e preencher

# ─── Google Search Console ───────────────────────────────────────────────────────
# A GSC API requer OAuth2 ou Service Account (não funciona com API key simples).
# Coloque o arquivo JSON do service account no diretório seo/ e configure o path:
GSC_SERVICE_ACCOUNT_FILE = os.getenv("GSC_SERVICE_ACCOUNT_FILE", "gsc_credentials.json")

# Propriedade no GSC (exatamente como aparece no painel)
GSC_SITE_URL = "sc-domain:ultramaquinas.com.br"

# Período de análise (dias para trás a partir de hoje)
GSC_DAYS_BACK = 90
GSC_ROW_LIMIT = 50  # máx de queries por URL

# ─── Claude API ─────────────────────────────────────────────────────────────────
CLAUDE_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
CLAUDE_MODEL = "claude-sonnet-5-20251001"

# ─── Configurações de pipeline ───────────────────────────────────────────────────
# Número de resultados orgânicos para análise de gap
SERP_RESULTS_TO_ANALYZE = 3

# Timeout para requisições HTTP (segundos)
REQUEST_TIMEOUT = 15

# Headers para fetch de páginas (simula browser)
FETCH_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
}

# ─── Output ─────────────────────────────────────────────────────────────────────
OUTPUT_DIR = "output"
OUTPUT_CSV = "output/resultados_seo.csv"
OUTPUT_JSON = "output/resultados_seo.json"
