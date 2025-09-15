
from .index import PolicyIndex

def retrieve_policy_snippets(cfg, question: str, top_k: int = 5):
    idx = PolicyIndex(cfg)
    return idx.search(question, top_k=top_k)
