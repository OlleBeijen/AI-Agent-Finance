
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from src.config import AppConfig

st.set_page_config(page_title="Instellingen", page_icon="⚙️", layout="wide")
st.title("⚙️ Instellingen")

cfg = AppConfig.load()
st.write("Paden")
st.json({
    "data": str(cfg.paths.data),
    "reports": str(cfg.paths.reports),
    "indexes": str(cfg.paths.indexes),
})
