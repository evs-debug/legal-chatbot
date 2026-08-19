import streamlit as st
from rag_engine import answer_question

st.set_page_config(page_title="Nyaya Setu", page_icon="⚖️", layout="wide")

TEXT = {
    "English": {
        "subtitle": "Constitutional Awareness & Legal Aid, grounded in the Constitution of India",
        "mode_header": "⚙️ Mode",
        "simple_mode": "🗣️ Simple Mode",
        "lawyer_mode": "⚖️ Lawyer Mode",
        "language_header": "🌐 Language",
        "examples_header": "💡 Examples",
        "about_header": "ℹ️ About",
        "about_text": "Answers are generated using RAG over the Constitution of India (Part III, IV & IVA). This is informational only, not a substitute for professional legal advice.",
        "input_placeholder": "Ask about your constitutional rights...",
        "spinner": "Consulting the Constitution...",
        "examples": [
            "What are my rights if I get arrested?",
            "Do I have the right to free education?",
            "Can the government stop me from practicing my religion?",
            "What does equality before law mean?",
            "Can I be forced to work without pay?",
            "What rights protect children from labour?",
        ]
    },
    "Hindi": {
        "subtitle": "संवैधानिक जागरूकता और कानूनी सहायता, भारत के संविधान पर आधारित",
        "mode_header": "⚙️ मोड",
        "simple_mode": "🗣️ सरल मोड",
        "lawyer_mode": "⚖️ वकील मोड",
        "language_header": "🌐 भाषा",
        "examples_header": "💡 उदाहरण",
        "about_header": "ℹ️ जानकारी",
        "about_text": "उत्तर भारत के संविधान (भाग III, IV और IVA) पर आधारित RAG तकनीक से तैयार किए जाते हैं। यह केवल सूचनात्मक है, पेशेवर कानूनी सलाह का विकल्प नहीं है।",
        "input_placeholder": "अपने संवैधानिक अधिकारों के बारे में पूछें...",
        "spinner": "संविधान से परामर्श किया जा रहा है...",
        "examples": [
            "गिरफ्तार होने पर मेरे क्या अधिकार हैं?",
            "क्या मुझे मुफ्त शिक्षा का अधिकार है?",
            "क्या सरकार मुझे मेरा धर्म मानने से रोक सकती है?",
            "कानून के समक्ष समानता का क्या अर्थ है?",
            "क्या मुझे बिना वेतन के काम करने पर मजबूर किया जा सकता है?",
            "बाल श्रम से बच्चों की सुरक्षा कौन से अधिकार करते हैं?",
        ]
    }
}

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Inter:wght@400;500;600&family=Noto+Sans+Devanagari:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap');

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
[data-testid="stSidebar"] * { color: var(--ink) !important; font-family: 'Inter', 'Noto Sans Devanagari', sans-serif !important; }

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
    font-family: 'Inter', 'Noto Sans Devanagari', sans-serif; font-size: 0.82rem;
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
    font-family: 'Inter', 'Noto Sans Devanagari', sans-serif !important;
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

[data-testid="stSidebar"] .stButton > button {
    width: 100%; text-align: left;
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    font-family: 'Inter', 'Noto Sans Devanagari', sans-serif !important;
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
    font-family: 'Inter', 'Noto Sans Devanagari', sans-serif !important;
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

div[data-baseweb="radio"] label { color: var(--ink) !important; font-family: 'Inter', 'Noto Sans Devanagari', sans-serif !important; }

footer, #MainMenu { visibility: hidden; }

/* Fix broken Material Symbols icon text (shows raw names when font fails to load) */
[data-testid="stSidebarCollapseButton"] span,
[data-testid="stSidebarCollapseButton"] p,
[data-testid="baseButton-headerNoPadding"] span,
.material-symbols-rounded,
.material-symbols-outlined,
[class*="material-icons"] {
    font-size: 0 !important;
    line-height: 0 !important;
}
[data-testid="stSidebarCollapseButton"] {
    position: relative;
}
[data-testid="stSidebarCollapseButton"]::after {
    content: "◀";
    font-size: 0.9rem !important;
    color: var(--ink);
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
}
</style>
""", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_query" not in st.session_state:
    st.session_state.pending_query = None
if "ui_language" not in st.session_state:
    st.session_state.ui_language = "English"

with st.sidebar:
    st.markdown("### 🌐 Language / भाषा")
    ui_language = st.radio(
        "UI language",
        ["English", "Hindi"],
        label_visibility="collapsed",
        key="ui_language"
    )

t = TEXT[ui_language]

st.markdown(f"""
<div class="header-wrap">
    <div class="chakra"></div>
    <div>
        <p class="title-text">Nyaya Setu</p>
        <p class="subtitle-text">{t['subtitle']}</p>
    </div>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("---")
    st.markdown(f"### {t['mode_header']}")
    mode_label = st.radio(
        "Response style",
        [t["simple_mode"], t["lawyer_mode"]],
        label_visibility="collapsed"
    )
    mode = "simple" if mode_label == t["simple_mode"] else "lawyer"

    st.markdown("---")
    st.markdown(f"### {t['examples_header']}")
    for q in t["examples"]:
        if st.button(q, key=q):
            st.session_state.pending_query = q

    st.markdown("---")
    st.markdown(f"### {t['about_header']}")
    st.caption(t["about_text"])

for msg in st.session_state.messages:
    avatar = "🧑" if msg["role"] == "user" else "⚖️"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])
        if msg["role"] == "assistant" and "sources" in msg:
            badges = "".join(
                f'<span class="seal-badge"><span class="seal-num">{s["clause"]}</span>{s["title"]}</span>'
                for s in msg["sources"]
            )
            st.markdown(badges, unsafe_allow_html=True)

typed_query = st.chat_input(t["input_placeholder"])
query = st.session_state.pending_query or typed_query
st.session_state.pending_query = None

if query:
    st.session_state.messages.append({"role": "user", "content": query})
    with st.chat_message("user", avatar="🧑"):
        st.markdown(query)

    with st.chat_message("assistant", avatar="⚖️"):
        with st.spinner(t["spinner"]):
            answer, sources = answer_question(query, mode=mode, language=ui_language)
            st.markdown(answer)
            badges = "".join(
                f'<span class="seal-badge"><span class="seal-num">{s["clause"]}</span>{s["title"]}</span>'
                for s in sources
            )
            st.markdown(badges, unsafe_allow_html=True)

    st.session_state.messages.append({"role": "assistant", "content": answer, "sources": sources})
