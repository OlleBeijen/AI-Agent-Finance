
# 💊 Creditnote Doctor — Streamlit AI Agent

Een tool om creditnota’s te analyseren en de onderliggende procesfouten zichtbaar te maken. Focus op prijs-, hoeveelheid-, leverdatum- en referentiefouten. Uitkomst: een wekelijks rapport met top-5 patronen per product en per klant, plus een korte management-samenvatting.

## Waarom
- Herhaalproblemen met directe euro-impact en duidelijke KPI’s (aantal creditnota’s, foutcategorieën, herstelkosten).
- Gericht op processen in plaats van losse documenten.
- Past bij “AI als APK”: vaste checks geven snel inzicht waar het fout gaat.
- Unieke insteek: clustering van faalpatronen en RAG over eigen policy’s.

## MVP-scope
**Input:** CSV-exporten uit Exact/AFAS/Twinfield (creditnota’s, factuurregels, orders, klanten, producten).  
**Detectie:** prijs/hoeveelheid/leverdatum/referentie + patronen per product/klant.  
**Output:** wekelijks rapport (Markdown/HTML) en korte samenvatting met acties.  
**Data:** lokale verwerking; optionele RAG over interne policy’s.  
**Deploy:** self-hosted (bijv. VM of Docker).

---

## Snel starten
1) Vereisten: Python 3.10+  
2) Installeer pakketten:
```bash
pip install -r requirements.txt
```
3) Zet variabelen:
```bash
cp .env.example .env
```
4) Start:
```bash
streamlit run app/streamlit_app.py
```
5) Laad voorbeelddata:
```bash
python scripts/seed_sample_data.py
```

### Docker
```
docker build -t creditnote-doctor .
docker run -p 8501:8501 -e ENV=prod creditnote-doctor
```
Of via compose: zie `docker/docker-compose.yml`.

---

## Mapstructuur
```
app/                 # Streamlit UI + pagina's
config/              # YAML-config en promptsjablonen
docs/                # Architectuur, deploy, data dictionary
sample_data/         # Voorbeeld CSV's + policy markdown
src/
  agent/             # Agent en workflows
  analysis/          # Regels, clustering, KPI's
  data/              # Loaders, validators, joiners
  rag/               # Eenvoudige TF-IDF index + search
  reporting/         # Rapport generatie en export
  utils/             # IO, logging, hashing
tests/               # Unit tests (pytest)
scripts/             # Handige scripts (seed, report)
```
Alles draait lokaal. Paden zijn in `config/config.yaml` te wijzigen of via `.env` variabelen.

---

## CSV-format
Zie **docs/DATA_DICTIONARY.md** voor kolommen per bestand. Minimale set:
- `invoices.csv`
- `credit_notes.csv`
- `orders.csv`
- `customers.csv`
- `products.csv`

De samples in `sample_data/` tonen het formaat.

---

## Analyse in het kort
- **Detectie:** heuristieken voor prijs/hoeveelheid/leverdatum/referentie op basis van joins tussen credit, factuur en order.
- **Clustering:** TF-IDF + k-means over tekst (oorzaak + reason_text) om terugkerende patronen te vinden.
- **KPI’s:** aantal creditregels, unieke creditnota’s, geschat herstelbedrag, verdeling per oorzaak.
- **Rapport:** Markdown en HTML in `reports/` (zie pagina *Wekelijks Rapport*).

### RAG over policy’s
- Index bouw je met TF-IDF (lokaal, geen internet nodig) via de pagina *Policies RAG* of `scripts/build_index.py`.
- Zo kun je per vraag de meest relevante stukken uit je eigen policy’s zien.

---

## Zelf uitbreiden
### Nieuwe oorzaakregel toevoegen
1. Voeg een regel toe in `src/analysis/rules.py` (functie `detect_root_causes`).
2. Leg de logica vast (bijv. controle op staffels of een bepaald referentiepatroon).
3. Voeg een test toe in `tests/` en run `pytest`.

### Meer features
- Maak nieuwe features in `src/analysis/features.py`.
- Gebruik ze bij prioritering of clustering.

### Extra pagina
- Voeg een file toe in `app/pages/` met prefix `X_` en een emoji voor sortering.

### Externe LLM (optioneel)
- Zet `rag.use_llm: true` en vul je sleutel in `.env` (OPENAI_API_KEY).  
- In de MVP wordt geen externe call gedaan; de basis werkt zonder.

---

## Beveiliging en privacy
- Data blijft lokaal in `data/`.
- Hash klant-ID’s met `security.hash_salt` als je dat wil.
- Houd logging beperkt en zonder PII.

---

## Testen
```
pytest -q
```

---

## Support
Open een issue of breid de documentatie in `docs/` uit. 
