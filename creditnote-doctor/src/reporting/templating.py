
from jinja2 import Template
import pandas as pd

def render_patterns_table(df: pd.DataFrame) -> str:
    if df is None or len(df) == 0:
        return "Geen patronen gevonden."
    return df.to_markdown(index=False)

def render_report_md(kpis: dict, top_prod, top_cust) -> str:
    tpl = Template("""
# Wekelijks Rapport — Creditnote Doctor

## KPI's
- Aantal creditregels: **{{ kpis.n_credit_lines }}**
- Unieke creditnota's: **{{ kpis.n_credit_notes }}**
- Geschat herstelbedrag: **€ {{ '%.2f' % kpis.estimated_recovery_eur }}**

### Verdeling per oorzaak
{% for k, v in kpis.by_cause.items() -%}
- {{ k }}: {{ v }}
{% endfor %}

## Top-5 patronen per product
{{ top_prod_md }}

## Top-5 patronen per klant
{{ top_cust_md }}
""")
    return tpl.render(
        kpis=kpis,
        top_prod_md=render_patterns_table(top_prod),
        top_cust_md=render_patterns_table(top_cust),
    )
