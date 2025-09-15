
import pandas as pd
from src.config import AppConfig
from src.data.loaders import load_all_inputs
from src.analysis.rules import detect_root_causes
from src.analysis.kpi import compute_kpis
from pathlib import Path
import json

cfg = AppConfig.load()
data = load_all_inputs(cfg.paths.data)
df = detect_root_causes(data, cfg)
kpis = compute_kpis(df)
Path(cfg.paths.reports).mkdir(parents=True, exist_ok=True)
(Path(cfg.paths.reports) / "kpis.json").write_text(json.dumps(kpis, indent=2), encoding="utf-8")
print("KPI's geëxporteerd naar reports/kpis.json")
