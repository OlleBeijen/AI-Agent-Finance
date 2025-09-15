
from pathlib import Path
import json
from .splitter import split_markdown
from .embed import TfidfEmbedder

class PolicyIndex:
    def __init__(self, cfg):
        self.cfg = cfg
        self.index_dir = cfg.paths.indexes
        self.embedder = TfidfEmbedder()
        self.docs = []
        self.X = None

    def _collect_texts(self):
        policy_dir = Path("sample_data/policies")
        texts = []
        meta = []
        for p in policy_dir.glob("*.md"):
            t = p.read_text(encoding="utf-8")
            chunks = split_markdown(t)
            for i, ch in enumerate(chunks):
                texts.append(ch)
                meta.append({"source": p.name, "chunk": i})
        return texts, meta

    def build_index(self):
        texts, meta = self._collect_texts()
        if not texts:
            return 0
        self.X = self.embedder.fit_transform(texts)
        self.docs = [{"text": t, **m} for t, m in zip(texts, meta)]
        # persist
        self.index_dir.mkdir(parents=True, exist_ok=True)
        (self.index_dir / "tfidf_vocab.json").write_text(json.dumps(list(self.embedder.get_feature_names())), encoding="utf-8")
        (self.index_dir / "docs.json").write_text(json.dumps(self.docs), encoding="utf-8")
        return len(self.docs)

    def _load_if_needed(self):
        if self.X is not None and self.docs:
            return
        docs_path = self.index_dir / "docs.json"
        vocab_path = self.index_dir / "tfidf_vocab.json"
        if not docs_path.exists() or not vocab_path.exists():
            self.build_index()
            return
        import json
        self.docs = json.loads(docs_path.read_text(encoding="utf-8"))
        from sklearn.feature_extraction.text import TfidfVectorizer
        vocab = json.loads(vocab_path.read_text(encoding="utf-8"))
        self.embedder = TfidfEmbedder()
        self.embedder.vectorizer.vocabulary_ = {t:i for i,t in enumerate(vocab)}
        self.embedder.vectorizer.fixed_vocabulary_ = True
        texts = [d["text"] for d in self.docs]
        self.X = self.embedder.transform(texts)

    def search(self, query: str, top_k: int = 5):
        self._load_if_needed()
        q = self.embedder.transform([query])
        # cosine similarity
        import numpy as np
        from sklearn.metrics.pairwise import cosine_similarity
        sims = cosine_similarity(q, self.X)[0]
        idx = np.argsort(-sims)[:top_k]
        results = []
        for i in idx:
            d = self.docs[i]
            results.append({"score": float(sims[i]), "source": d["source"], "snippet": d["text"][:300]})
        return results
