import json
import pickle
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index(os.path.join(BASE_DIR, "articles.index"))
with open(os.path.join(BASE_DIR, "articles_meta.pkl"), "rb") as f:
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

def build_history_text(chat_history):
    if not chat_history:
        return ""
    recent = chat_history[-6:]
    lines = []
    for msg in recent:
        role = "User" if msg["role"] == "user" else "Assistant"
        lines.append(f"{role}: {msg['content']}")
    return "\n".join(lines)


def answer_question(query, mode="simple", language="English", chat_history=None):
    search_query = query
    if chat_history:
        last_user_msgs = [m["content"] for m in chat_history[-4:] if m["role"] == "user"]
        if last_user_msgs:
            search_query = " ".join(last_user_msgs[-1:] + [query])

    results = retrieve(search_query, top_k=4)
    context = build_context(results)

    system_prompt = SYSTEM_PROMPTS.get(mode, SYSTEM_PROMPTS["simple"])
    system_prompt += "\n\nIf the user's question refers back to something discussed earlier in the conversation (e.g. 'what about as a minor', 'and if it's non-bailable'), use the conversation history provided to understand what they're referring to, while still grounding your legal answer in the retrieved context below."

    if language == "Hindi":
        system_prompt += "\n\nRespond entirely in Hindi (Devanagari script), including all explanations. Keep clause numbers and article numbers in their original English/numeric form (e.g. 'Clause 22(1)'), since these are standard legal references, but everything else must be in Hindi."

    history_text = build_history_text(chat_history)
    history_block = f"Recent conversation:\n{history_text}\n\n" if history_text else ""

    user_prompt = f"""{history_block}Context (relevant constitutional provisions):
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


def analyze_document(document_text, language="English"):
    """Analyze an uploaded legal document and extract key info + next steps."""
    max_chars = 12000
    truncated = document_text[:max_chars]
    truncation_note = "\n\n[Note: document was truncated for analysis due to length.]" if len(document_text) > max_chars else ""

    system_prompt = """You are a legal document analysis assistant for India. A user has uploaded a legal document (e.g. notice, contract, FIR copy, court order, agreement).
Analyze it and provide:
1. **Document Type** - what kind of document this appears to be
2. **Key Information** - important names, dates, deadlines, amounts, and obligations mentioned
3. **Plain-Language Summary** - what this document means in simple terms
4. **Recommended Next Steps** - concrete, practical actions the person should consider taking, including whether they should consult a lawyer urgently

Be factual and only summarize what is actually in the document - do not invent details. If the document is unclear, low quality, or not actually a legal document, say so honestly.
This is informational only and not a substitute for professional legal advice - make this clear in your next steps section."""

    if language == "Hindi":
        system_prompt += "\n\nRespond entirely in Hindi (Devanagari script)."

    user_prompt = f"""Document text:
{truncated}{truncation_note}

Analyze this document."""

    response = groq_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
    )

    return response.choices[0].message.content
