
from sklearn.feature_extraction.text import TfidfVectorizer

class TfidfEmbedder:
    def __init__(self, max_features=2000):
        self.vectorizer = TfidfVectorizer(max_features=max_features)

    def fit_transform(self, texts):
        return self.vectorizer.fit_transform(texts)

    def transform(self, texts):
        return self.vectorizer.transform(texts)

    def get_feature_names(self):
        return self.vectorizer.get_feature_names_out()
