import streamlit as st
import requests

# Set page configuration
st.set_page_config(
    page_title="🎙️ AI Audiobook Narrator", 
    page_icon="📖", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@700&display=swap');
    
    /* Main Title Styles */
    .big-title {
        font-size: 3.8rem !important;
        font-family: 'Poppins', sans-serif !important;
        text-align: center !important;
        background: linear-gradient(45deg, #FF6B6B, #8A2BE2, #6366f1) !important;
        -webkit-background-clip: text !important;
        background-clip: text !important;
        color: transparent !important;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.2) !important;
        margin: 0.8rem 0 !important;
        letter-spacing: 1px !important;
        line-height: 1.2 !important;
    }
    
    /* Button Styles */
    .stButton>button {
        background: linear-gradient(135deg, #FF6B6B 0%, #8A2BE2 50%, #6366f1 100%) !important;
        color: white !important;
        font-size: 18px !important;
        padding: 12px 28px !important;
        border-radius: 8px !important;
        border: none !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    .stButton>button:hover {
        background: linear-gradient(135deg, #6366f1 0%, #8A2BE2 50%, #FF6B6B 100%) !important;
        transform: scale(1.05) !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
    }
    
    .stDownloadButton>button {
        background: linear-gradient(135deg, #10b981 0%, #06b6d4 50%, #3b82f6 100%) !important;
        color: white !important;
        font-size: 16px !important;
        padding: 10px 24px !important;
        border-radius: 8px !important;
        border: none !important;
        transition: all 0.3s ease-in-out !important;
    }
    
    /* Sidebar Styles */
    .sidebar-header {
        background: linear-gradient(135deg, #FF6B6B 0%, #8A2BE2 50%, #6366f1 100%);
        color: white !important;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        font-family: 'Poppins', sans-serif;
    }
    
    .sidebar-header h2 {
        margin: 0;
        font-size: 1.5rem;
        font-weight: 600;
        letter-spacing: 0.5px;
    }
    
    .sidebar-text {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        margin: 15px 0 8px !important;
        color: #4A4A4A !important;
        padding: 5px 0 !important;
        position: relative;
        display: flex;
        align-items: center;
    }

    .sidebar-text span {
        background: linear-gradient(90deg, #FF6B6B 0%, #8A2BE2 100%);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent !important;
    }

    .sidebar-text::before {
        content: attr(data-emoji);
        margin-right: 8px;
        filter: drop-shadow(2px 2px 2px rgba(0,0,0,0.1));
        font-style: normal !important;
    }
    
    .stSelectbox [data-testid='stMarkdownContainer'] {
        font-size: 1rem !important;
        font-weight: 500 !important;
    }
    
    .stSlider [role='slider'] {
        background: #8A2BE2 !important;
    }
    
    .stSelectbox:hover div:first-child {
        background: rgba(255,255,255,0.95) !important;
        border: 1px solid #FF6B6B !important;
        transition: all 0.2s ease;
    }
    
    /* Global Styles */
    body {
        background: linear-gradient(135deg, #fff1eb 0%, #ace0f9 100%) !important;
    }
    
    .stTextArea textarea {
        background: rgba(255,255,255,0.9) !important;
        border-radius: 10px !important;
        font-size: 16px !important;
        padding: 15px !important;
    }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown("""
    <div class="big-title">
        🎙️ AI Audiobook Narrator
    </div>
""", unsafe_allow_html=True)

# Language and voice configuration
LANGUAGE_VOICE_MAP = {
    "US English": ("us", [
        "af_heart", "af_alloy", "af_aoede", "af_bella", "af_jessica",
        "af_kore", "af_nicole", "af_nova", "af_river", "af_sarah", "af_sky",
        "am_adam", "am_echo", "am_eric", "am_fenrir", "am_liam",
        "am_michael", "am_onyx", "am_puck", "am_santa"
    ]),
    "UK English": ("uk", [
        "bf_alice", "bf_emma", "bf_isabella", "bf_lily",
        "bm_daniel", "bm_fable", "bm_george", "bm_lewis"
    ]),
    "Japanese": ("jp", [
        "jf_alpha", "jf_gongitsune", "jf_nezumi", "jf_tebukuro",
        "jm_kumo"
    ]),
    "Mandarin Chinese": ("zh", [
        "zf_xiaobei", "zf_xiaoni", "zf_xiaoxiao", "zf_xiaoyi",
        "zm_yunjian", "zm_yunxi", "zm_yunxia", "zm_yunyang"
    ]),
    "Spanish": ("es", [
        "ef_dora", "em_alex", "em_santa"
    ]),
    "French": ("fr", [
        "ff_siwis"
    ]),
    "Hindi": ("hi", [
        "hf_alpha", "hf_beta", "hm_omega", "hm_psi"
    ]),
    "Italian": ("it", [
        "if_sara", "im_nicola"
    ]),
    "Brazilian Portuguese": ("pt", [
        "pf_dora", "pm_alex", "pm_santa"
    ])
}

# Sidebar controls
st.sidebar.markdown("""
    <div class="sidebar-header">
        <h2>✨ Creative Voice Studio 🎶</h2>
        <p style="margin:5px 0 0; font-size:0.9rem;">Craft Your Perfect Narration</p>
    </div>
""", unsafe_allow_html=True)

# Language selection
st.sidebar.markdown(
    '<div class="sidebar-text" data-emoji="🌍"><span>Select Language</span></div>', 
    unsafe_allow_html=True
)
language = st.sidebar.selectbox("", list(LANGUAGE_VOICE_MAP.keys()), label_visibility="collapsed")

# Voice selection
lang_code, voices = LANGUAGE_VOICE_MAP[language]
st.sidebar.markdown(
    '<div class="sidebar-text" data-emoji="🎤"><span>Choose Voice Style</span></div>', 
    unsafe_allow_html=True
)
voice = st.sidebar.selectbox("", voices, label_visibility="collapsed")

# Speed control
st.sidebar.markdown(
    '<div class="sidebar-text" data-emoji="⏩"><span>Narration Speed</span></div>', 
    unsafe_allow_html=True
)
speed = st.sidebar.slider("", 0.5, 2.0, 1.0, label_visibility="collapsed", help="Adjust speech speed.")

# Main content area
text = st.text_area("📝 Enter the text to convert into speech:", height=150, help="Paste your text here (max 5000 characters).")

# Audio generation logic
if st.button("🎙️ Generate Audiobook", key="generate"):
    if not text.strip():
        st.warning("⚠️ Please enter some text before generating the audiobook.")
    else:
        with st.spinner("⏳ Processing... Generating audiobook..."):
            try:
                response = requests.post(
                    "http://localhost:8000/narrate/",
                    json={"text": text, "voice": voice, "lang": lang_code, "speed": speed},
                    timeout=60
                )
                
                if response.status_code == 200:
                    result = response.json()
                    st.success("✅ Audiobook successfully generated!")
                    st.audio(result["audio_file"], format="audio/wav")
                    
                    with open(result["audio_file"], "rb") as f:
                        st.download_button(
                            "⬇️ Download Audiobook",
                            f,
                            file_name="audiobook.wav",
                            mime="audio/wav",
                            key="download-audio"
                        )
                else:
                    st.error(f"❌ API Error: {response.status_code} - {response.text}")

            except requests.exceptions.RequestException as e:
                st.error(f"🚨 Connection Error: {str(e)}")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    '<p style="text-align:center; font-size:16px; color:#2E2E2E;">Made with ❤️ by Krishna Priya Nynaru, an AI Developer</p>',
    unsafe_allow_html=True
)