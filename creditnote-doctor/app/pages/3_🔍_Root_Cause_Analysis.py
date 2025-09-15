
import streamlit as st
import pandas as pd
from src.config import AppConfig
from src.agent.agent import CreditnoteDoctorAgent
from src.data.loaders import load_all_inputs
from src.analysis.rules import detect_root_causes
from src.analysis.kpi import compute_kpis
from src.analysis.clustering import cluster_failure_patterns
from src.reporting.templating import render_patterns_table

st.set_page_config(page_title="Analyse", page_icon="🔍", layout="wide")
st.title("🔍 Root Cause Analyse")

cfg = AppConfig.load()
agent = CreditnoteDoctorAgent(cfg)

data = load_all_inputs(cfg.paths.data)
if data is None:
    st.error("Geen data gevonden in de data-map. Upload eerst je CSV's.")
    st.stop()

causes_df = detect_root_causes(data, cfg)
kpis = compute_kpis(causes_df)

st.subheader("KPI's")
col1, col2, col3 = st.columns(3)
col1.metric("Aantal creditregels", int(kpis['n_credit_lines']))
col2.metric("Unieke creditnota's", int(kpis['n_credit_notes']))
col3.metric("Geschat herstelbedrag", f"€ {kpis['estimated_recovery_eur']:.2f}")

st.subheader("Top-5 faalpatronen per product")
patterns_prod = cluster_failure_patterns(causes_df, by='product_id', top_k=5)
st.dataframe(patterns_prod)

st.subheader("Top-5 faalpatronen per klant")
patterns_cust = cluster_failure_patterns(causes_df, by='customer_id', top_k=5)
st.dataframe(patterns_cust)

st.download_button("Exporteer patronen (CSV)", data=patterns_prod.to_csv(index=False), file_name="patterns_products.csv")
