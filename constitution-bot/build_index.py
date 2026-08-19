import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

with open("data.json", "r", encoding="utf-8") as f:
    articles = json.load(f)

texts = []
for a in articles:
    plain = a.get("plain_language", "")
    tags = " ".join(a.get("tags", []))
    combined = f"Article {a['clause']}: {a['title']}. {a['text']} {plain} Tags: {tags}"
    texts.append(combined)

print(f"Embedding {len(texts)} clauses...")

model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(texts, show_progress_bar=True)
embeddings = np.array(embeddings).astype("float32")

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

faiss.write_index(index, "articles.index")
with open("articles_meta.pkl", "wb") as f:
    pickle.dump(articles, f)

print("Done. Saved articles.index and articles_meta.pkl")
