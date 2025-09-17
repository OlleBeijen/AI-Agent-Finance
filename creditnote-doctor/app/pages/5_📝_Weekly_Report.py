
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from src.config import AppConfig
from src.agent.agent import CreditnoteDoctorAgent
from src.reporting.generate_weekly import generate_weekly_report

st.set_page_config(page_title="Wekelijks Rapport", page_icon="📝", layout="wide")
st.title("📝 Wekelijks Rapport")

cfg = AppConfig.load()
agent = CreditnoteDoctorAgent(cfg)

if st.button("Genereer rapport"):
    report_paths = generate_weekly_report(cfg)
    if report_paths:
        md_path, html_path = report_paths
        with open(md_path, "r", encoding="utf-8") as f:
            st.markdown(f.read())
        with open(html_path, "r", encoding="utf-8") as f:
            st.download_button("Download HTML", data=f.read(), file_name="weekly_report.html")
    else:
        st.error("Rapport generatie mislukt. Controleer of data aanwezig is.")
