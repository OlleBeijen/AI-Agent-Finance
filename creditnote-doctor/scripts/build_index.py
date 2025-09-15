
from src.config import AppConfig
from src.rag.index import PolicyIndex

cfg = AppConfig.load()
idx = PolicyIndex(cfg)
print(f"Documenten geindexeerd: {idx.build_index()}")
