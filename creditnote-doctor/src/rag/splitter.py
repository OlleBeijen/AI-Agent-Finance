
from typing import List
import re

def split_markdown(text: str, max_len: int = 1200) -> List[str]:
    # Heel eenvoudige splitter op headings en lengtes
    parts = re.split(r"\n\s*#.+\n", text)
    out = []
    buf = ""
    for p in parts:
        if len(buf) + len(p) < max_len:
            buf += "\n" + p
        else:
            if buf.strip():
                out.append(buf.strip())
            buf = p
    if buf.strip():
        out.append(buf.strip())
    return [x for x in out if x.strip()]
