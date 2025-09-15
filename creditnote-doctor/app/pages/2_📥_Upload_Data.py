
import streamlit as st
from src.utils.io import save_uploaded_file
from src.config import AppConfig
from src.agent.agent import CreditnoteDoctorAgent

st.set_page_config(page_title="Upload Data", page_icon="📥", layout="wide")
st.title("📥 Upload Data")

cfg = AppConfig.load()
agent = CreditnoteDoctorAgent(cfg)

st.write("Upload CSV's: facturen, creditnota's, orders, klanten, producten.")

for name in ["invoices.csv","credit_notes.csv","orders.csv","customers.csv","products.csv"]:
    file = st.file_uploader(f"Upload {name}", type=["csv"], key=name)
    if file:
        path = save_uploaded_file(file, cfg.paths.data / name)
        st.success(f"Opgeslagen: {path}")

st.info("Geüploade bestanden worden gevalideerd en genormaliseerd bij Analyse.")
