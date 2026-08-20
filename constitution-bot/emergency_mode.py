"""
emergency_mode.py

Renders the "I need help right now" Emergency Legal Mode for Ordo Juris.
Bilingual: pass language="English" or language="Hindi" to each render function.
"""

import streamlit as st
from emergency_scenarios import EMERGENCY_SCENARIOS_BY_LANG

UI_TEXT = {
    "English": {
        "sidebar_button": "🚨 I need help right now",
        "banner_title": "Emergency Legal Mode",
        "banner_body": "If you are in immediate physical danger, call 112 first. This mode gives quick, situation-specific guidance grounded in the Constitution and Indian law.",
        "whats_happening": "What's happening?",
        "picker_caption": "Pick the situation closest to yours. You'll get clear, actionable guidance — not a wall of legal text.",
        "not_listed_caption": "Don't see your situation above?",
        "describe_placeholder": "e.g. My neighbour is blocking my property entrance",
        "not_listed_button": "My situation isn't listed — ask Ordo Juris",
        "back_button": "Back to normal chat",
        "know_header": "What you should know",
        "do_header": "What you can do",
        "not_do_header": "What NOT to do",
        "rights_header": "Your rights",
        "help_header": "Get help",
        "disclaimer": "This is general information, not legal advice for your specific case. For anything serious, please contact a lawyer or the helplines above.",
        "followup_caption": "Have a follow-up question about this situation?",
        "followup_placeholder": "e.g. What if I'm a minor?",
        "followup_button": "Ask Ordo Juris",
        "different_situation": "Choose a different situation",
        "exit_button": "Exit emergency mode",
    },
    "Hindi": {
        "sidebar_button": "🚨 मुझे अभी मदद चाहिए",
        "banner_title": "आपातकालीन कानूनी मोड",
        "banner_body": "अगर आप तत्काल शारीरिक खतरे में हैं, तो पहले 112 पर कॉल करें। यह मोड संविधान और भारतीय कानून पर आधारित त्वरित, स्थिति-विशिष्ट मार्गदर्शन देता है।",
        "whats_happening": "क्या हो रहा है?",
        "picker_caption": "अपनी स्थिति के सबसे करीब वाली स्थिति चुनें। आपको स्पष्ट, कार्रवाई योग्य मार्गदर्शन मिलेगा — कानूनी शब्दों की दीवार नहीं।",
        "not_listed_caption": "ऊपर अपनी स्थिति नहीं दिख रही?",
        "describe_placeholder": "जैसे, मेरा पड़ोसी मेरी संपत्ति के प्रवेश द्वार को अवरुद्ध कर रहा है",
        "not_listed_button": "मेरी स्थिति सूचीबद्ध नहीं है — Ordo Juris से पूछें",
        "back_button": "सामान्य चैट पर वापस जाएं",
        "know_header": "आपको क्या पता होना चाहिए",
        "do_header": "आप क्या कर सकते हैं",
        "not_do_header": "क्या न करें",
        "rights_header": "आपके अधिकार",
        "help_header": "मदद प्राप्त करें",
        "disclaimer": "यह सामान्य जानकारी है, आपके विशिष्ट मामले के लिए कानूनी सलाह नहीं है। किसी भी गंभीर मामले के लिए, कृपया वकील या ऊपर दी गई हेल्पलाइनों से संपर्क करें।",
        "followup_caption": "इस स्थिति के बारे में कोई फॉलो-अप सवाल है?",
        "followup_placeholder": "जैसे, अगर मैं नाबालिग हूं तो क्या होगा?",
        "followup_button": "Ordo Juris से पूछें",
        "different_situation": "एक अलग स्थिति चुनें",
        "exit_button": "आपातकालीन मोड से बाहर निकलें",
    },
}


def render_emergency_button(language="English"):
    ui = UI_TEXT[language]
    st.markdown("---")
    if st.button(ui["sidebar_button"], use_container_width=True, type="primary"):
        st.session_state["emergency_active"] = True
        st.session_state["emergency_situation"] = None
        st.rerun()


def _situation_picker(language):
    ui = UI_TEXT[language]
    scenarios = EMERGENCY_SCENARIOS_BY_LANG[language]

    st.subheader(ui["whats_happening"])
    st.caption(ui["picker_caption"])

    cols = st.columns(2)
    keys = list(scenarios.keys())
    for i, key in enumerate(keys):
        scenario = scenarios[key]
        col = cols[i % 2]
        with col:
            if st.button(scenario["title"], key=f"emergency_pick_{key}", use_container_width=True):
                st.session_state["emergency_situation"] = key
                st.rerun()

    st.markdown("---")
    st.caption(ui["not_listed_caption"])
    with st.form(key="emergency_fallback_form", clear_on_submit=True):
        free_text = st.text_input(
            "Describe",
            placeholder=ui["describe_placeholder"],
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button(ui["not_listed_button"], use_container_width=True)

    if submitted:
        if free_text.strip():
            prefill = (
                "I need urgent help and my situation wasn't in the emergency list. "
                f"Here's what's happening: {free_text.strip()}. "
                "Please explain what I should know, what I can do, what to avoid, "
                "my relevant constitutional/legal rights, and where I can get help."
            )
        else:
            prefill = (
                "I need urgent help and my situation wasn't in the emergency list. "
                "Please ask me what's happening and then explain what I should know, "
                "what I can do, what to avoid, my relevant rights, and where to get help."
            )
        st.session_state["pending_prefill"] = prefill
        st.session_state["emergency_active"] = False
        st.session_state["emergency_situation"] = None
        st.rerun()

    st.markdown("---")
    if st.button(ui["back_button"]):
        st.session_state["emergency_active"] = False
        st.session_state["emergency_situation"] = None
        st.rerun()


def _situation_detail(key, language):
    ui = UI_TEXT[language]
    scenario = EMERGENCY_SCENARIOS_BY_LANG[language][key]

    st.subheader(scenario["title"])

    st.markdown(f"#### {ui['know_header']}")
    for item in scenario["what_to_know"]:
        st.markdown(f"- {item}")

    st.markdown(f"#### {ui['do_header']}")
    for item in scenario["what_you_can_do"]:
        st.markdown(f"- {item}")

    st.markdown(f"#### {ui['not_do_header']}")
    for item in scenario["what_not_to_do"]:
        st.markdown(f"- {item}")

    st.markdown(f"#### {ui['rights_header']}")
    for r in scenario["your_rights"]:
        st.markdown(f"- **{r['article']}** — {r['desc']}")

    st.markdown(f"#### {ui['help_header']}")
    for h in scenario["get_help"]:
        st.markdown(f"- **{h['name']}**: {h['contact']}")

    st.info(ui["disclaimer"])

    st.markdown("---")
    st.caption(ui["followup_caption"])
    with st.form(key=f"followup_form_{key}", clear_on_submit=True):
        followup = st.text_input(
            "Follow-up",
            placeholder=ui["followup_placeholder"],
            label_visibility="collapsed",
        )
        followup_submitted = st.form_submit_button(ui["followup_button"], use_container_width=True)

    if followup_submitted and followup.strip():
        prefill = (
            f"Regarding the situation '{scenario['title']}': {followup.strip()}"
        )
        st.session_state["pending_prefill"] = prefill
        st.session_state["emergency_active"] = False
        st.session_state["emergency_situation"] = None
        st.rerun()

    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        if st.button(ui["different_situation"]):
            st.session_state["emergency_situation"] = None
            st.rerun()
    with col2:
        if st.button(ui["exit_button"]):
            st.session_state["emergency_active"] = False
            st.session_state["emergency_situation"] = None
            st.rerun()


def render_emergency_mode(language="English"):
    ui = UI_TEXT[language]
    st.markdown(
        f"""
        <div style="background-color:#7a2e2e; padding:12px 16px; border-radius:8px; margin-bottom:16px;">
            <span style="color:white; font-size:1.1em; font-weight:600;">
                {ui['banner_title']}
            </span>
            <br>
            <span style="color:#f0d9d9; font-size:0.9em;">
                {ui['banner_body']}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    situation = st.session_state.get("emergency_situation")
    if situation is None:
        _situation_picker(language)
    else:
        _situation_detail(situation, language)
