import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
        .stApp { background: radial-gradient(circle at 50% 50%, #0d1117 0%, #010409 100%); color: #00d4ff; }
        .main-title { font-family: 'Orbitron', sans-serif; color: #00d4ff; text-shadow: 0 0 20px rgba(0, 212, 255, 0.6); font-size: 3rem; font-weight: 700; text-align: center; }
        .system-header { font-family: 'Courier New', monospace; color: #ff00ff; text-shadow: 0 0 8px #ff00ff; font-size: 0.8rem; text-align: center; letter-spacing: 2px; }
        div[data-testid="stForm"], .stMetric { background: rgba(0, 212, 255, 0.02) !important; border: 1px solid rgba(0, 212, 255, 0.2) !important; backdrop-filter: blur(15px); border-radius: 10px; }
        .stButton>button { background: transparent !important; color: #00d4ff !important; border: 2px solid #00d4ff !important; font-family: 'Orbitron', sans-serif; transition: 0.4s; width: 100%; }
        .stButton>button:hover { background: #00d4ff !important; color: #000 !important; box-shadow: 0 0 30px #00d4ff; }
        #MainMenu, footer, header {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)

def render_header():
    st.markdown("""
        <div style="text-align: center; padding: 10px;">
            <svg width="60" height="60" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M12 2L4.5 20.29L5.21 21L12 18L18.79 21L19.5 20.29L12 2Z" stroke="#00d4ff" stroke-width="1.5"/>
                <circle cx="12" cy="12" r="3" stroke="#ff00ff" stroke-width="1"/>
            </svg>
            <p class="system-header">NEURAL_ENGINE_CORE // ACTIVE</p>
            <h1 class="main-title">NEUROVERDICT</h1>
        </div>
    """, unsafe_allow_html=True)