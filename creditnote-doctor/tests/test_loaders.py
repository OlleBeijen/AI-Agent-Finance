
from src.data.loaders import load_all_inputs
from src.config import AppConfig

def test_load_all_inputs():
    cfg = AppConfig.load()
    data = load_all_inputs(cfg.paths.data if cfg.paths.data.exists() else cfg.paths.data)
    assert data is None or isinstance(data, dict)
