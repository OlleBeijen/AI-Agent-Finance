
import sys
from pathlib import Path

# Zorg dat projectroot (met 'src/') in sys.path staat wanneer de app vanuit app/ draait
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from src.config import AppConfig
from src.agent.agent import CreditnoteDoctorAgent
from src.utils.io import ensure_dirs

st.set_page_config(
    page_title="Creditnote Doctor",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.title("Creditnote Doctor 💊")
st.sidebar.info("Analyseer creditnota's en vind procesoorzaken")

cfg = AppConfig.load()
ensure_dirs(cfg)

if 'agent' not in st.session_state:
    st.session_state.agent = CreditnoteDoctorAgent(cfg)

st.title("Dashboard")
st.write("Welkom! Ga via de pagina's links door de stappen: upload → analyse → rapport.")
st.page_link("pages/2_📥_Upload_Data.py", label="Ga naar Upload", icon="📥")
st.page_link("pages/3_🔍_Root_Cause_Analysis.py", label="Ga naar Analyse", icon="🔍")
st.page_link("pages/5_📝_Weekly_Report.py", label="Ga naar Rapport", icon="📝")
