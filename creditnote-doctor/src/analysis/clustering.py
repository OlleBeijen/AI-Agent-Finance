
import pandas as pd

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.cluster import KMeans

    _SKLEARN = True
except Exception:
    _SKLEARN = False


def cluster_failure_patterns(df: pd.DataFrame, by: str, top_k: int = 5) -> pd.DataFrame:
    # Combineer oorzaak + reason_text voor eenvoudige patroonvorming
    df = df.copy()
    df["text"] = (df["root_cause"].fillna("") + " " + df.get("reason_text", "").astype(str))
    texts = df["text"].tolist()
    if len(texts) == 0:
        return pd.DataFrame(columns=[by,"cluster","count","top_terms"])

    if _SKLEARN:
        vec = TfidfVectorizer(max_features=1000, ngram_range=(1,2))
        X = vec.fit_transform(texts)
        n_clusters = max(1, min(8, len(texts)//5))  # eenvoudige keuze
        km = KMeans(n_clusters=n_clusters, n_init="auto", random_state=42)
        labels = km.fit_predict(X)
        df["cluster"] = labels
        # Top termen per cluster
        terms = vec.get_feature_names_out()
        centroids = km.cluster_centers_
        top_terms = []
        for i in range(n_clusters):
            idx = centroids[i].argsort()[-5:][::-1]
            top_terms.append(", ".join(terms[idx]))
        cluster_terms = {i: t for i, t in enumerate(top_terms)}
    else:
        # Fallback zonder sklearn: groepeer op 'root_cause' + grof patroon (eerste 2 woorden)
        df["cluster"] = (
            df["text"].str.split().apply(lambda x: " ".join(x[:2]) if len(x) else "n/a")
        )
        keys = {k: i for i, k in enumerate(sorted(df["cluster"].astype(str).unique()))}
        df["cluster"] = df["cluster"].map(keys)
        cluster_terms = {v: k for k, v in keys.items()}

    summary = (
        df.groupby([by,"cluster"])
          .size()
          .reset_index(name="count")
          .sort_values(["count"], ascending=False)
    )
    summary["top_terms"] = summary["cluster"].map(cluster_terms)
    # per 'by' de top K
    out = summary.sort_values(["count"], ascending=[False]).groupby(by).head(top_k).reset_index(drop=True)
    return out
