import streamlit as st
from rag_engine import answer_question

st.set_page_config(page_title="Nyaya Setu", page_icon="⚖️", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap');

:root {
    --bg: #F2EBDC;
    --surface: #FAF6EC;
    --surface-alt: #E9DCC3;
    --brown: #6B4226;
    --brown-bright: #8B5A2B;
    --ink: #2B241C;
    --ink-muted: #786F5E;
    --border: rgba(107,66,38,0.25);
}

html, body, .stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stHeader"],
[data-testid="stBottom"],
[data-testid="stBottomBlockContainer"],
.main .block-container {
    background: var(--bg) !important;
}

[data-testid="stSidebar"] {
    background: var(--surface-alt) !important;
    border-right: 1px solid var(--border);
}
[data-testid="stSidebar"] * { color: var(--ink) !important; }

.header-wrap {
    display: flex; align-items: center; gap: 0.85rem;
    padding: 0.5rem 0 1rem 0;
    border-bottom: 1px solid var(--border);
    margin-bottom: 1.4rem;
}
.chakra {
    width: 44px; height: 44px; flex-shrink: 0; border-radius: 50%;
    border: 1.5px solid var(--brown);
    background: repeating-conic-gradient(var(--brown) 0deg 2deg, transparent 2deg 15deg);
    position: relative;
}
.chakra::after {
    content: ""; position: absolute; inset: 14px;
    background: var(--bg); border-radius: 50%; border: 1px solid var(--brown);
}
.title-text {
    font-family: 'Fraunces', serif; font-size: 2.35rem; font-weight: 600;
    color: var(--ink); margin: 0; line-height: 1.1;
}
.subtitle-text {
    font-family: 'Inter', sans-serif; font-size: 0.82rem;
    color: var(--ink-muted); margin: 4px 0 0 0;
}

[data-testid="stChatMessage"] {
    background: var(--surface) !important;
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 4px 8px;
}
[data-testid="stChatMessage"] p,
[data-testid="stChatMessage"] li,
[data-testid="stChatMessage"] span,
[data-testid="stChatMessage"] div,
[data-testid="stChatMessage"] strong,
[data-testid="stChatMessage"] em,
[data-testid="stChatMessage"] ol,
[data-testid="stChatMessage"] ul,
[data-testid="stChatMessage"] h1,
[data-testid="stChatMessage"] h2,
[data-testid="stChatMessage"] h3,
[data-testid="stChatMessage"] h4 {
    font-family: 'Inter', sans-serif !important;
    color: var(--ink) !important;
    line-height: 1.6;
}
[data-testid="stChatMessage"] strong { color: var(--ink) !important; font-weight: 700; }

.seal-badge {
    display: inline-flex; align-items: center; gap: 8px;
    background: var(--surface-alt);
    border: 1px solid var(--brown);
    border-radius: 999px;
    padding: 6px 14px 6px 10px;
    margin: 4px 6px 4px 0;
    font-family: 'IBM Plex Mono', monospace;
    font-size: 0.78rem;
    color: var(--brown-bright);
}
.seal-num {
    background: var(--brown);
    color: var(--surface);
    border-radius: 50%;
    width: 20px; height: 20px;
    display: inline-flex; align-items: center; justify-content: center;
    font-size: 0.68rem; font-weight: 700;
}

/* Sidebar example-question buttons — high specificity to beat Streamlit defaults */
[data-testid="stSidebar"] .stButton > button {
    width: 100%; text-align: left;
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.85rem !important;
}
[data-testid="stSidebar"] .stButton > button p,
[data-testid="stSidebar"] .stButton > button div,
[data-testid="stSidebar"] .stButton > button span {
    color: var(--ink) !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
    border-color: var(--brown) !important;
    background: var(--bg) !important;
}
[data-testid="stSidebar"] .stButton > button:hover p {
    color: var(--brown-bright) !important;
}

/* Chat input bar */
[data-testid="stChatInput"],
[data-testid="stChatInput"] > div,
[data-testid="stChatInputContainer"],
.stChatInputContainer,
[data-testid="stBottomBlockContainer"] > div {
    background: var(--brown) !important;
    border: 1px solid var(--brown) !important;
    border-radius: 12px !important;
}
[data-testid="stChatInput"] textarea {
    background: var(--brown) !important;
    color: var(--surface) !important;
}
[data-testid="stChatInput"] textarea::placeholder {
    color: rgba(250,246,236,0.65) !important;
}
[data-testid="stChatInput"] button {
    background: var(--brown-bright) !important;
    border: none !important;
}
[data-testid="stChatInput"] button svg {
    fill: var(--surface) !important;
}

[data-testid="stSidebar"] h3 {
    font-size: 0.95rem !important;
}
[data-testid="stSidebar"] .stCaption,
[data-testid="stSidebar"] [data-testid="stCaptionContainer"] p {
    font-size: 0.72rem !important;
    line-height: 1.4 !important;
}

div[data-baseweb="radio"] label { color: var(--ink) !important; font-family: 'Inter', sans-serif !important; }

footer, #MainMenu { visibility: hidden; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header-wrap">
    <div class="chakra"></div>
    <div>
        <p class="title-text">Nyaya Setu</p>
        <p class="subtitle-text">Constitutional Awareness &amp; Legal Aid, grounded in the Constitution of India</p>
    </div>
</div>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_query" not in st.session_state:
    st.session_state.pending_query = None

with st.sidebar:
    st.markdown("### ⚙️ Mode")
    mode_label = st.radio(
        "Response style",
        ["🗣️ Simple Mode", "⚖️ Lawyer Mode"],
        label_visibility="collapsed"
    )
    mode = "simple" if "Simple" in mode_label else "lawyer"

    st.markdown("---")
    st.markdown("### 💡 Examples")
    example_questions = [
        "What are my rights if I get arrested?",
        "Do I have the right to free education?",
        "Can the government stop me from practicing my religion?",
        "What does equality before law mean?",
        "Can I be forced to work without pay?",
        "What rights protect children from labour?",
    ]
    for q in example_questions:
        if st.button(q, key=q):
            st.session_state.pending_query = q

    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.caption(
        "Answers are generated using RAG over the Constitution of India "
        "(Part III & related articles). This is informational only, "
        "not a substitute for professional legal advice."
    )

for msg in st.session_state.messages:
    avatar = "🧑" if msg["role"] == "user" else "⚖️"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and "sources" in msg:
            badges = "".join(
                f'<span class="seal-badge"><span class="seal-num">{s["article_number"]}</span>{s["title"]}</span>'
                for s in msg["sources"]
            )
            st.markdown(badges, unsafe_allow_html=True)

typed_query = st.chat_input("Ask about your constitutional rights...")
query = st.session_state.pending_query or typed_query
st.session_state.pending_query = None

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(query)

    with st.chat_message("assistant", avatar="⚖️"):
        with st.spinner("Consulting the Constitution..."):
            answer, sources = answer_question(query, mode=mode)
            st.markdown(answer)
            badges = "".join(
                f'<span class="seal-badge"><span class="seal-num">{s["article_number"]}</span>{s["title"]}</span>'
                for s in sources
            )
            st.markdown(badges, unsafe_allow_html=True)

    st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})
