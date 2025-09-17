
from pathlib import Path
import html


def save_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path

def md_to_html(md_text: str) -> str:
    """
    Zet Markdown om naar HTML. Als 'markdown' pakket niet aanwezig is,
    val terug op een simpele weergave zodat de app niet crasht.
    """
    try:
        import markdown  # type: ignore
    except Exception:
        # Fallback: toon ruwe markdown veilig ge-escaped
        safe = html.escape(md_text).replace("\n", "<br>")
        return f"<div style='white-space:normal;font-family:system-ui,Arial'>{safe}</div>"
    else:
        return markdown.markdown(md_text, extensions=["tables"])
