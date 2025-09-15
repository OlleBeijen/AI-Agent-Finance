
import streamlit as st
from src.config import AppConfig
from src.rag.index import PolicyIndex

st.set_page_config(page_title="Policies RAG", page_icon="📚", layout="wide")
st.title("📚 Policies RAG")

cfg = AppConfig.load()
idx = PolicyIndex(cfg)

st.write("Bouw of herbouw de index over interne policy's en procesbeschrijvingen.")
if st.button("Rebuild index"):
    n = idx.build_index()
    st.success(f"Index gebouwd met {n} documenten.")

query = st.text_input("Vraag over policy/processen")
if query:
    results = idx.search(query, top_k=5)
    for r in results:
        st.write(f"- {r['score']:.3f} — {r['source']}")
        st.caption(r['snippet'])
