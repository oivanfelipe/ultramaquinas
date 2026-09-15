"""
Exportadores de resultado do pipeline SEO.

- export_excel: gera XLSX com URL, SEO Title, Meta Description
- export_google_doc: cria Google Doc via Drive API (requer GOOGLE_SERVICE_ACCOUNT_FILE
  ou credenciais OAuth configuradas) com descrição em dois formatos
- build_html_description: monta HTML da descrição a partir do JSON do ESPECIALISTA
"""

import datetime
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from config import OUTPUT_DIR, GOOGLE_DOCS_SERVICE_ACCOUNT_FILE


# ─── Helpers ─────────────────────────────────────────────────────────────────

def build_html_description(result: dict) -> str:
    """Converte o bloco 'descricao' do JSON em HTML para colar no CMS."""
    d = result.get("descricao", {})
    if not d:
        return ""

    parts = []

    if d.get("h2"):
        parts.append(f"<h2>{d['h2']}</h2>")

    if d.get("intro"):
        parts.append(f"<p>{d['intro']}</p>")

    for section in d.get("h3_sections", []):
        if section.get("h3"):
            parts.append(f"<h3>{section['h3']}</h3>")

        if section.get("content"):
            parts.append(f"<p>{section['content']}</p>")

        bullets = section.get("bullets", [])
        if bullets:
            items = "".join(f"<li>{b}</li>" for b in bullets)
            parts.append(f"<ul>{items}</ul>")

        for h4s in section.get("h4_sections", []):
            if h4s.get("h4"):
                parts.append(f"<h4>{h4s['h4']}</h4>")
            if h4s.get("content"):
                parts.append(f"<p>{h4s['content']}</p>")

    if d.get("conclusao"):
        parts.append(f"<p>{d['conclusao']}</p>")

    return "\n".join(parts)


def build_plain_description(result: dict) -> str:
    """Versão legível (sem tags) da descrição para revisão."""
    d = result.get("descricao", {})
    if not d:
        return ""

    lines = []

    if d.get("h2"):
        lines.append(d["h2"].upper())
        lines.append("")

    if d.get("intro"):
        lines.append(d["intro"])
        lines.append("")

    for section in d.get("h3_sections", []):
        if section.get("h3"):
            lines.append(f"— {section['h3']}")

        if section.get("content"):
            lines.append(section["content"])

        for b in section.get("bullets", []):
            lines.append(f"  • {b}")

        for h4s in section.get("h4_sections", []):
            if h4s.get("h4"):
                lines.append(f"  {h4s['h4']}")
            if h4s.get("content"):
                lines.append(f"  {h4s['content']}")

        lines.append("")

    if d.get("conclusao"):
        lines.append(d["conclusao"])

    return "\n".join(lines).strip()


# ─── Excel ───────────────────────────────────────────────────────────────────

def export_excel(results: list, path: str = None) -> str:
    """
    Exporta Excel com colunas: URL | Keyword | SEO Title | Meta Description.
    Retorna o caminho do arquivo gerado.
    """
    import openpyxl
    from openpyxl.styles import Font, PatternFill, Alignment

    path = path or os.path.join(OUTPUT_DIR, "seo_metadata.xlsx")

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "SEO Metadata"

    header_font = Font(bold=True, color="FFFFFF")
    header_fill = PatternFill("solid", fgColor="1A1A2E")
    wrap = Alignment(wrap_text=True, vertical="top")

    headers = ["URL", "Keyword Principal", "SEO Title", "Chars Title", "Meta Description", "Chars Meta", "Erro"]
    col_widths = [50, 30, 55, 12, 100, 12, 40]

    for col, (h, w) in enumerate(zip(headers, col_widths), 1):
        cell = ws.cell(row=1, column=col, value=h)
        cell.font = header_font
        cell.fill = header_fill
        cell.alignment = wrap
        ws.column_dimensions[cell.column_letter].width = w

    for row_idx, r in enumerate(results, 2):
        values = [
            r.get("url", ""),
            r.get("keyword_principal", ""),
            r.get("seo_title", ""),
            r.get("seo_title_chars", ""),
            r.get("meta_description", ""),
            r.get("meta_description_chars", ""),
            r.get("error", ""),
        ]
        for col, val in enumerate(values, 1):
            cell = ws.cell(row=row_idx, column=col, value=val)
            cell.alignment = wrap

    ws.freeze_panes = "A2"
    wb.save(path)
    return path


# ─── Google Doc ──────────────────────────────────────────────────────────────

def _get_docs_service(sa_file: str):
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

    creds = service_account.Credentials.from_service_account_file(
        sa_file,
        scopes=[
            "https://www.googleapis.com/auth/documents",
            "https://www.googleapis.com/auth/drive.file",
        ],
    )
    docs = build("docs", "v1", credentials=creds)
    drive = build("drive", "v3", credentials=creds)
    return docs, drive


def _build_doc_requests(results: list) -> list:
    """
    Monta a lista de requests para a Docs API (batchUpdate).
    Estrutura por produto:
      [TÍTULO DO PRODUTO]
      SEO Title / Meta / Keyword
      ── Descrição Padrão ──
      (texto legível)
      ── HTML ──
      (código HTML)
      ────────────────────
    """
    requests_list = []
    cursor = 1  # posição de inserção no documento (começa em 1)

    def insert(text, style=None):
        nonlocal cursor
        req = {
            "insertText": {
                "location": {"index": cursor},
                "text": text,
            }
        }
        requests_list.append(req)

        if style:
            requests_list.append({
                "updateParagraphStyle": {
                    "range": {
                        "startIndex": cursor,
                        "endIndex": cursor + len(text),
                    },
                    "paragraphStyle": {"namedStyleType": style},
                    "fields": "namedStyleType",
                }
            })

        cursor += len(text)

    ts = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    header = f"SEO Ultra Máquinas — Rodada {ts}\n"
    insert(header, "HEADING_1")

    for r in results:
        if r.get("error") and not r.get("seo_title"):
            insert(f"\n[ERRO] {r.get('url', '')}: {r.get('error', '')}\n")
            continue

        product_title = r.get("keyword_principal") or r.get("url", "")
        insert(f"\n{product_title}\n", "HEADING_2")

        insert(f"URL: {r.get('url', '')}\n")
        insert(f"Keyword: {r.get('keyword_principal', '')}\n")
        insert(f"SEO Title: {r.get('seo_title', '')} ({r.get('seo_title_chars', '')} chars)\n")
        insert(f"Meta Description: {r.get('meta_description', '')} ({r.get('meta_description_chars', '')} chars)\n")

        insert("\nDescrição — Formato Padrão\n", "HEADING_3")
        plain = build_plain_description(r)
        insert(plain + "\n")

        insert("\nDescrição — HTML\n", "HEADING_3")
        html = build_html_description(r)
        insert(html + "\n")

        insert("\n" + "─" * 60 + "\n")

    return requests_list


def export_google_doc(results: list, sa_file: str = None, share_with: str = None) -> str:
    """
    Cria um Google Doc com as descrições em formato padrão e HTML.
    sa_file: Service Account JSON com permissão Docs + Drive.
    share_with: e-mail para compartilhar o documento (opcional).
    Retorna a URL do documento criado.
    """
    sa_file = sa_file or GOOGLE_DOCS_SERVICE_ACCOUNT_FILE
    if not sa_file or not os.path.exists(sa_file):
        raise FileNotFoundError(
            f"Service Account para Google Docs não encontrada: {sa_file}. "
            "Configure GOOGLE_DOCS_SERVICE_ACCOUNT_FILE no .env"
        )

    docs_svc, drive_svc = _get_docs_service(sa_file)

    ts = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    title = f"SEO Ultra Máquinas — {ts}"

    doc = docs_svc.documents().create(body={"title": title}).execute()
    doc_id = doc["documentId"]

    requests_list = _build_doc_requests(results)
    if requests_list:
        docs_svc.documents().batchUpdate(
            documentId=doc_id,
            body={"requests": requests_list},
        ).execute()

    if share_with:
        drive_svc.permissions().create(
            fileId=doc_id,
            body={"type": "user", "role": "writer", "emailAddress": share_with},
            sendNotificationEmail=False,
        ).execute()

    return f"https://docs.google.com/document/d/{doc_id}/edit"
