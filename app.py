import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(
    page_title="NEUROVERDICT | Neural Engine",
    page_icon="⚡", 
    layout="wide"
)

# 2. Advanced CSS & Neural Logo Injection
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

    .stApp {
        background: radial-gradient(circle at 50% 50%, #0d1117 0%, #010409 100%);
        color: #00d4ff;
    }

    /* System Flicker Animation */
    @keyframes flicker {
        0% { opacity: 0.8; }
        50% { opacity: 1; }
        100% { opacity: 0.9; }
    }

    .system-header {
        font-family: 'Courier New', monospace;
        color: #ff00ff;
        text-shadow: 0 0 8px #ff00ff;
        font-size: 0.85rem;
        animation: flicker 2s infinite;
        letter-spacing: 2px;
    }

    /* Unique Title Font */
    .main-title {
        font-family: 'Orbitron', sans-serif;
        color: #00d4ff;
        text-shadow: 0 0 20px rgba(0, 212, 255, 0.6);
        font-size: 3.5rem;
        font-weight: 700;
        margin-top: -10px;
    }

    /* Glass Container Styling */
    div[data-testid="stForm"], .stMetric, .stAlert, div[data-testid="stExpander"] {
        background: rgba(0, 212, 255, 0.02) !important;
        border: 1px solid rgba(0, 212, 255, 0.2) !important;
        border-radius: 10px !important;
        box-shadow: 0 0 30px rgba(0, 0, 0, 0.5);
        backdrop-filter: blur(15px);
    }

    /* Interactive Button */
    .stButton>button {
        background: transparent !important;
        color: #00d4ff !important;
        border: 2px solid #00d4ff !important;
        border-radius: 0px !important; /* Sharp industrial corners */
        font-family: 'Orbitron', sans-serif;
        height: 4em;
        transition: 0.4s all;
        text-transform: uppercase;
    }

    .stButton>button:hover {
        background: #00d4ff !important;
        color: #000 !important;
        box-shadow: 0 0 40px #00d4ff !important;
    }

    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Setup Groq Client 
# Leave this blank at the top or initialize as None
client = None

if "neuro_analysis" not in st.session_state:
    st.session_state.neuro_analysis = None

# --- APP UI ---

# Custom SVG Logo + Title
st.markdown("""
    <div style="text-align: center; padding: 20px;">
        <svg width="80" height="80" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M12 2L4.5 20.29L5.21 21L12 18L18.79 21L19.5 20.29L12 2Z" stroke="#00d4ff" stroke-width="1" stroke-linejoin="round" style="filter: drop-shadow(0 0 5px #00d4ff);"/>
            <circle cx="12" cy="12" r="3" stroke="#ff00ff" stroke-width="1" style="filter: drop-shadow(0 0 8px #ff00ff);"/>
        </svg>
        <p class="system-header">NEURAL_ENGINE_CORE // OPTIMIZATION_MODE</p>
        <h1 class="main-title">NEUROVERDICT</h1>
    </div>
    """, unsafe_allow_html=True)

# Sidebar Diagnostics
with st.sidebar:
    st.markdown("### 🧪 SYSTEM LOGS")
    # ADD THIS LINE BELOW:
    api_key_input = st.text_input("ENTER GROQ KEY", type="password")
    
    st.code("INITIALIZING CORE...\nLOAD: LLAMA_3.1\nSTATUS: STABLE", language="bash")
    st.divider()
    st.write("Arbitrating link hierarchy through deep neural processing.")

# Input Section
with st.form("neuro_form"):
    col1, col2 = st.columns(2)
    with col1:
        url_a = st.text_input("💠 SOURCE ALPHA")
    with col2:
        url_b = st.text_input("💠 SOURCE BETA")
    
    analyze = st.form_submit_button("EXECUTE VERDICT")

# Analysis Logic
if analyze:
    if not api_key_input:
        st.error("🔑 ACCESS DENIED: Please enter your Groq API Key in the sidebar.")
    elif url_a and url_b:
        with st.spinner("⚡ SYNTHESIZING DATA NODES..."):
            try:
                # Initialize client inside the button click
                client = Groq(api_key=api_key_input)
                
                prompt = f"Analyze and compare these two product links: {url_a} and {url_b}. Give a neuro-marketing conversion score (0-100) for each, identify triggers, and pick a winner."
                
                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}],
                )
                st.session_state.neuro_analysis = completion.choices[0].message.content
            except Exception as e:
                st.error(f"RUNTIME ERROR: {e}")
    else:
        st.warning("⚠️ CRITICAL: Two inputs required for data collation.")

# Results Display
if st.session_state.neuro_analysis:
    st.markdown("### 📡 TRANSMISSION RECEIVED")
    
    m1, m2, m3 = st.columns(3)
    m1.metric("ALPHA YIELD", "84%", "STABLE")
    m2.metric("BETA YIELD", "71%", "-13%", delta_color="inverse")
    m3.metric("NEURAL SYNC", "99.4%", "ACTIVE")

    st.divider()
    st.markdown(st.session_state.neuro_analysis)

    f1, f2 = st.columns(2)
    with f1:
        st.download_button("📂 SAVE ARCHIVE", st.session_state.neuro_analysis, "neuro_verdict.txt", use_container_width=True)
    with f2:
        if st.button("☣️ SYSTEM RESET", use_container_width=True):
            st.session_state.neuro_analysis = None
            st.rerun()