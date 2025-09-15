
from dataclasses import dataclass
from pathlib import Path
import os
import yaml

@dataclass
class Paths:
    data: Path
    reports: Path
    indexes: Path

@dataclass
class AppConfig:
    env: str
    paths: Paths
    analysis: dict
    rag: dict
    security: dict

    @staticmethod
    def load(config_path: Path | None = None) -> "AppConfig":
        if config_path is None:
            config_path = Path("config/config.yaml")
        with open(config_path, "r", encoding="utf-8") as f:
            raw = yaml.safe_load(f)
        def env_or_default(key, default):
            return os.getenv(key, default)
        data = Path(env_or_default("DATA_DIR", raw["paths"]["data"]))
        reports = Path(env_or_default("REPORT_DIR", raw["paths"]["reports"]))
        indexes = Path(env_or_default("INDEX_DIR", raw["paths"]["indexes"]))
        return AppConfig(
            env=os.getenv("ENV", raw.get("env", "dev")),
            paths=Paths(data=data, reports=reports, indexes=indexes),
            analysis=raw.get("analysis", {}),
            rag=raw.get("rag", {}),
            security=raw.get("security", {}),
        )
