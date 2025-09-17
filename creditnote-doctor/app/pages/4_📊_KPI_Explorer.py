
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import pandas as pd
from src.config import AppConfig
from src.data.loaders import load_csv_safe

st.set_page_config(page_title="KPI Explorer", page_icon="📊", layout="wide")
st.title("📊 KPI Explorer")

cfg = AppConfig.load()
credit = load_csv_safe(cfg.paths.data / "credit_notes.csv")
if credit is not None:
    st.dataframe(credit.head(1000))
else:
    st.info("Upload eerst credit_notes.csv")
