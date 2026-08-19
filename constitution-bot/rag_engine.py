import json
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("articles.index")
with open("articles_meta.pkl", "rb") as f:
    articles = pickle.load(f)

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def retrieve(query, top_k=3):
    query_vec = embed_model.encode([query]).astype("float32")
    distances, indices = index.search(query_vec, top_k)
    results = [articles[i] for i in indices[0]]
    return results

def build_context(results):
    context = ""
    for a in results:
        context += f"Clause {a['clause']} ({a['title']}) — {a['part']}:\n"
        context += f"Text: {a['text']}\n"
        if a.get("plain_language"):
            context += f"Plain meaning: {a['plain_language']}\n"
        if a.get("landmark_cases"):
            context += f"Landmark cases: {'; '.join(a['landmark_cases'])}\n"
        context += "\n"
    return context

SYSTEM_PROMPTS = {
    "simple": """You are a Constitutional Awareness and Legal Aid assistant for India.
Answer the user's question using ONLY the constitutional provisions given in the context below.
Explain it in simple, plain language a non-lawyer can understand, like you're explaining it to a friend.
Always cite the specific clause number(s) you used.
If the context does not contain enough information to answer confidently, say so clearly and recommend the user consult a legal professional. Do not make up information.""",

    "lawyer": """You are a Constitutional Awareness and Legal Aid assistant for India, responding in a formal legal register.
Answer the user's question using ONLY the constitutional provisions given in the context below.
Use precise legal terminology and reference clause numbers explicitly.
Keep the answer compact: NEVER use a two-column or table format. Structure as a short numbered list, one clause per item, each item at most 2 sentences (provision + effect combined, not separated). No long quoted blocks of the provision text - paraphrase it concisely instead.
If landmark case law is provided in the context and is directly relevant, cite it in one short clause at the end of the relevant point, not as a separate section.
If the context does not contain enough information to answer confidently, state this explicitly and recommend consultation with a qualified legal professional. Do not fabricate legal information or case citations."""
}

def answer_question(query, mode="simple"):
    results = retrieve(query, top_k=4)
    context = build_context(results)

    system_prompt = SYSTEM_PROMPTS.get(mode, SYSTEM_PROMPTS["simple"])

    user_prompt = f"""Context (relevant constitutional provisions):
{context}

Question: {query}

Answer citing the clause number(s)."""

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
    )

    answer = response.choices[0].message.content
    return answer, results

if __name__ == "__main__":
    q = "What are my rights if I get arrested?"
    answer, sources = answer_question(q, mode="simple")
    print("QUESTION:", q)
    print("\nANSWER:\n", answer)
    print("\nSOURCES USED:")
    for s in sources:
        print(f"- Clause {s['clause']}: {s['title']}")
