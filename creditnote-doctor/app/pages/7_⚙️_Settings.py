
import streamlit as st
from src.config import AppConfig
from pathlib import Path

st.set_page_config(page_title="Instellingen", page_icon="⚙️", layout="wide")
st.title("⚙️ Instellingen")

cfg = AppConfig.load()
st.write("Paden")
st.json({
    "data": str(cfg.paths.data),
    "reports": str(cfg.paths.reports),
    "indexes": str(cfg.paths.indexes),
})
