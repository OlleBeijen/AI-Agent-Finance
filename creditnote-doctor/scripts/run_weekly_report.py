
from src.config import AppConfig
from src.reporting.generate_weekly import generate_weekly_report

cfg = AppConfig.load()
paths = generate_weekly_report(cfg)
print(f"Rapport paden: {paths}")
