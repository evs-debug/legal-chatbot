import streamlit as st
from rag_engine import answer_question, analyze_document
from pdf_utils import extract_text_from_pdf
from emergency_mode import render_emergency_button, render_emergency_mode

st.set_page_config(page_title="Ordo Juris", page_icon="⚖️", layout="wide")

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
        "tab_chat": "💬 Ask a Question",
        "tab_analyzer": "📄 Document Analyzer",
        "upload_label": "Upload a legal document (PDF)",
        "upload_help": "e.g. notice, contract, FIR copy, court order, agreement",
        "analyze_button": "Analyze Document",
        "analyzing_spinner": "Reading and analyzing your document...",
        "no_file_warning": "Please upload a PDF first.",
        "extract_fail": "Could not extract readable text from this PDF. It may be a scanned image without OCR.",
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
        "tab_chat": "💬 प्रश्न पूछें",
        "tab_analyzer": "📄 दस्तावेज़ विश्लेषक",
        "upload_label": "एक कानूनी दस्तावेज़ अपलोड करें (PDF)",
        "upload_help": "जैसे नोटिस, अनुबंध, एफआईआर प्रति, अदालत का आदेश",
        "analyze_button": "दस्तावेज़ का विश्लेषण करें",
        "analyzing_spinner": "आपके दस्तावेज़ को पढ़ा और विश्लेषण किया जा रहा है...",
        "no_file_warning": "कृपया पहले एक PDF अपलोड करें।",
        "extract_fail": "इस PDF से पठनीय टेक्स्ट निकाला नहीं जा सका। यह बिना OCR वाला स्कैन किया गया चित्र हो सकता है।",
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
    border-radius: 999px;
    min-width: 20px;
    height: 20px;
    padding: 0 6px;
    display: inline-flex; align-items: center; justify-content: center;
    font-size: 0.68rem; font-weight: 700;
    white-space: nowrap;
    flex-shrink: 0;
}
.seal-badge {
    flex-wrap: nowrap;
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

/* Custom tab-switcher buttons (main content area, NOT sidebar) — using Streamlit button type */
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-primary"] {
    background: var(--surface) !important;
    border: 1.5px solid var(--brown) !important;
    border-bottom: 3px solid var(--brown) !important;
    border-radius: 10px 10px 4px 4px !important;
    color: var(--brown) !important;
    font-weight: 600 !important;
    font-family: 'Inter', 'Noto Sans Devanagari', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 1.2rem !important;
    box-shadow: none !important;
}
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-primary"] p,
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-primary"] span,
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-primary"] div {
    color: var(--brown) !important;
    font-weight: 600 !important;
}
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-secondary"] {
    background: transparent !important;
    border: 1px solid var(--border) !important;
    border-radius: 10px 10px 4px 4px !important;
    color: var(--ink-muted) !important;
    font-family: 'Inter', 'Noto Sans Devanagari', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.6rem 1.2rem !important;
    box-shadow: none !important;
}
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-secondary"] p,
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-secondary"] span,
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-secondary"] div {
    color: var(--ink-muted) !important;
}
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-secondary"]:hover {
    border-color: var(--brown) !important;
    color: var(--brown) !important;
}
div[data-testid="stMainBlockContainer"] button[data-testid="stBaseButton-secondary"]:hover p {
    color: var(--brown) !important;
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

/* Main content area — general text color for markdown, headers, lists (covers emergency mode etc.) */
[data-testid="stMainBlockContainer"] h1,
[data-testid="stMainBlockContainer"] h2,
[data-testid="stMainBlockContainer"] h3,
[data-testid="stMainBlockContainer"] h4,
[data-testid="stMainBlockContainer"] h5,
[data-testid="stMainBlockContainer"] p,
[data-testid="stMainBlockContainer"] li,
[data-testid="stMainBlockContainer"] span,
[data-testid="stMainBlockContainer"] strong,
[data-testid="stMainBlockContainer"] em,
[data-testid="stMainBlockContainer"] label,
[data-testid="stMainBlockContainer"] .stMarkdown,
[data-testid="stMainBlockContainer"] [data-testid="stMarkdownContainer"] {
    color: var(--ink) !important;
}
[data-testid="stMainBlockContainer"] .stCaption,
[data-testid="stMainBlockContainer"] [data-testid="stCaptionContainer"] p {
    color: var(--ink-muted) !important;
}
/* st.info box styling */
[data-testid="stMainBlockContainer"] [data-testid="stAlert"] {
    background: var(--surface-alt) !important;
    border: 1px solid var(--border) !important;
}
[data-testid="stMainBlockContainer"] [data-testid="stAlert"] p,
[data-testid="stMainBlockContainer"] [data-testid="stAlert"] span {
    color: var(--ink) !important;
}
/* Text input fields (used in emergency fallback/followup forms) */
[data-testid="stMainBlockContainer"] input[type="text"] {
    background: var(--surface) !important;
    color: var(--ink) !important;
    border: 1px solid var(--border) !important;
}

/* Main content area — general text color for markdown, headers, lists (covers emergency mode etc.) */
[data-testid="stMainBlockContainer"] h1,
[data-testid="stMainBlockContainer"] h2,
[data-testid="stMainBlockContainer"] h3,
[data-testid="stMainBlockContainer"] h4,
[data-testid="stMainBlockContainer"] h5,
[data-testid="stMainBlockContainer"] p,
[data-testid="stMainBlockContainer"] li,
[data-testid="stMainBlockContainer"] span,
[data-testid="stMainBlockContainer"] strong,
[data-testid="stMainBlockContainer"] em,
[data-testid="stMainBlockContainer"] label,
[data-testid="stMainBlockContainer"] .stMarkdown,
[data-testid="stMainBlockContainer"] [data-testid="stMarkdownContainer"] {
    color: var(--ink) !important;
}
[data-testid="stMainBlockContainer"] .stCaption,
[data-testid="stMainBlockContainer"] [data-testid="stCaptionContainer"] p {
    color: var(--ink-muted) !important;
}
/* st.info box styling */
[data-testid="stMainBlockContainer"] [data-testid="stAlert"] {
    background: var(--surface-alt) !important;
    border: 1px solid var(--border) !important;
}
[data-testid="stMainBlockContainer"] [data-testid="stAlert"] p,
[data-testid="stMainBlockContainer"] [data-testid="stAlert"] span {
    color: var(--ink) !important;
}
/* Text input fields (used in emergency fallback/followup forms) */
[data-testid="stMainBlockContainer"] input[type="text"] {
    background: var(--surface) !important;
    color: var(--ink) !important;
    border: 1px solid var(--border) !important;
}

/* Form submit buttons (e.g. emergency mode follow-up forms) */
[data-testid="stFormSubmitButton"] button {
    background: transparent !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    color: var(--ink) !important;
    font-family: 'Inter', 'Noto Sans Devanagari', sans-serif !important;
}
[data-testid="stFormSubmitButton"] button p,
[data-testid="stFormSubmitButton"] button span,
[data-testid="stFormSubmitButton"] button div {
    color: var(--ink) !important;
}
[data-testid="stFormSubmitButton"] button:hover {
    border-color: var(--brown) !important;
    color: var(--brown) !important;
}
[data-testid="stFormSubmitButton"] button:hover p {
    color: var(--brown) !important;
}

footer, #MainMenu { visibility: hidden; }

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
if "active_tab" not in st.session_state:
    st.session_state.active_tab = "chat"

with st.sidebar:
    st.markdown("### 🌐 Language / भाषा")
    ui_language = st.radio(
        "UI language",
        ["English", "Hindi"],
        label_visibility="collapsed",
        key="ui_language"
    )

t = TEXT[ui_language]

if st.session_state.get("emergency_active"):
    render_emergency_mode(language=ui_language)
    st.stop()

st.markdown(f"""
<div class="header-wrap">
    <div class="chakra"></div>
    <div>
        <p class="title-text">Ordo Juris</p>
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
            st.session_state.active_tab = "chat"

    st.markdown("---")
    st.markdown(f"### {t['about_header']}")
    st.caption(t["about_text"])

    render_emergency_button(language=ui_language)

# Custom tab switcher
col_a, col_b, col_rest = st.columns([1.3, 1.3, 3])
with col_a:
    chat_type = "primary" if st.session_state.active_tab == "chat" else "secondary"
    if st.button(t["tab_chat"], key="tab_btn_chat", type=chat_type):
        st.session_state.active_tab = "chat"
        st.rerun()
with col_b:
    analyzer_type = "primary" if st.session_state.active_tab == "analyzer" else "secondary"
    if st.button(t["tab_analyzer"], key="tab_btn_analyzer", type=analyzer_type):
        st.session_state.active_tab = "analyzer"
        st.rerun()

st.markdown("<div style='border-bottom: 1px solid var(--border); margin-bottom: 1rem;'></div>", unsafe_allow_html=True)

if st.session_state.active_tab == "chat":
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
else:
    uploaded_file = st.file_uploader(t["upload_label"], type=["pdf"], help=t["upload_help"])
    if st.button(t["analyze_button"]):
        if uploaded_file is None:
            st.warning(t["no_file_warning"])
        else:
            with st.spinner(t["analyzing_spinner"]):
                doc_text = extract_text_from_pdf(uploaded_file)
                if not doc_text or len(doc_text.strip()) < 20:
                    st.error(t["extract_fail"])
                else:
                    analysis = analyze_document(doc_text, language=ui_language)
                    st.markdown(analysis)

# Chat input kept at top level so it stays pinned to the bottom of the page
typed_query = st.chat_input(t["input_placeholder"])
prefill = st.session_state.pop("pending_prefill", None)
query = prefill or st.session_state.pending_query or typed_query
st.session_state.pending_query = None

if query:
    st.session_state.active_tab = "chat"
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
    st.rerun()
