
from pathlib import Path
from dataclasses import dataclass
from ..config import AppConfig
from ..data.loaders import load_all_inputs
from ..analysis.rules import detect_root_causes
from ..analysis.kpi import compute_kpis
from ..analysis.clustering import cluster_failure_patterns
from .templating import render_report_md
from .exporter import save_text, md_to_html

def generate_weekly_report(cfg: AppConfig):
    data = load_all_inputs(cfg.paths.data)
    if data is None:
        return None
    df = detect_root_causes(data, cfg)
    kpis = compute_kpis(df)
    top_prod = cluster_failure_patterns(df, by='product_id', top_k=int(cfg.analysis.get("top_k_patterns",5)))
    top_cust = cluster_failure_patterns(df, by='customer_id', top_k=int(cfg.analysis.get("top_k_patterns",5)))
    md = render_report_md(kpis, top_prod, top_cust)
    reports_dir = cfg.paths.reports
    md_path = save_text(reports_dir / "weekly_report.md", md)
    html = md_to_html(md)
    html_path = save_text(reports_dir / "weekly_report.html", html)
    return md_path, html_path
