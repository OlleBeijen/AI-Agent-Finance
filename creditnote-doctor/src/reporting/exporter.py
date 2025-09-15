
from pathlib import Path

def save_text(path: Path, text: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path

def md_to_html(md_text: str) -> str:
    # heel simpele omzetting: paragrafen en koppen
    import markdown
    return markdown.markdown(md_text, extensions=["tables"])
