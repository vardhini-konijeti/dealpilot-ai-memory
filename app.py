import streamlit as st
import os
from groq import Groq
from hindsight_client import Hindsight
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="DealPilot AI — Enterprise Memory Studio",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# Premium Modern CSS: Inter typography, Glassmorphism, subtle gradients, polished cards
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Background and containers */
    .stApp {
        background: radial-gradient(circle at 15% 15%, #161b26 0%, #0b0f17 100%);
        color: #f1f5f9;
    }

    /* Top Brand Hero */
    .hero-container {
        padding: 1.5rem 0 1rem 0;
        margin-bottom: 1.5rem;
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
    }
    .brand-title {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #ffffff 0%, #94a3b8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: -0.03em;
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
    }
    .brand-badge {
        background: rgba(99, 102, 241, 0.15);
        border: 1px solid rgba(99, 102, 241, 0.35);
        color: #a5b4fc;
        font-size: 0.75rem;
        padding: 0.25rem 0.65rem;
        border-radius: 9999px;
        font-weight: 600;
        letter-spacing: 0.05em;
        text-transform: uppercase;
        vertical-align: middle;
        margin-left: 0.8rem;
    }
    .brand-sub {
        color: #94a3b8;
        font-size: 0.95rem;
        margin-top: 0.3rem;
    }

    /* Glass Cards */
    .studio-card {
        background: rgba(26, 32, 46, 0.65);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 1.25rem;
        backdrop-filter: blur(12px);
        margin-bottom: 1rem;
    }
    
    .card-title {
        font-size: 0.95rem;
        font-weight: 600;
        color: #cbd5e1;
        margin-bottom: 0.8rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }

    /* Comparison Result Panels */
    .output-box-augmented {
        background: rgba(16, 185, 129, 0.04);
        border: 1px solid rgba(16, 185, 129, 0.25);
        border-radius: 12px;
        padding: 1.25rem;
        min-height: 380px;
    }
    .output-box-stateless {
        background: rgba(239, 68, 68, 0.04);
        border: 1px solid rgba(239, 68, 68, 0.22);
        border-radius: 12px;
        padding: 1.25rem;
        min-height: 380px;
    }

    .output-header-aug {
        color: #34d399;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }
    .output-header-state {
        color: #f87171;
        font-size: 0.95rem;
        font-weight: 600;
        margin-bottom: 0.75rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }

    /* Sidebar Clean Styling */
    section[data-testid="stSidebar"] {
        background-color: #0d121c !important;
        border-right: 1px solid rgba(255, 255, 255, 0.06);
    }
    
    /* Memory Chip Tag */
    .memory-chip {
        background: rgba(59, 130, 246, 0.12);
        border: 1px solid rgba(59, 130, 246, 0.28);
        border-radius: 8px;
        padding: 0.7rem 0.9rem;
        margin-bottom: 0.6rem;
        font-size: 0.85rem;
        color: #93c5fd;
    }
</style>
""", unsafe_allow_html=True)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HINDSIGHT_BASE_URL = os.getenv("HINDSIGHT_BASE_URL", "https://api.hindsight.vectorize.io")
HINDSIGHT_API_KEY = os.getenv("HINDSIGHT_API_KEY")

groq_client = Groq(api_key=GROQ_API_KEY)
hindsight = Hindsight(base_url=HINDSIGHT_BASE_URL, api_key=HINDSIGHT_API_KEY)

BANK_ID = "dealpilot_sales_memory"

# ================= SIDEBAR: MEMORY VAULT & INGESTION =================
with st.sidebar:
    st.markdown("### 🧠 Memory Ingestion Hub")
    st.caption("Store client notes, objections, and company battlecards into persistent vector memory.")
    
    deal_name = st.text_input("Active Account / Deal", value="Rahul - Gym Membership")
    
    memory_type = st.radio("Context Type", ["Client Call / Note", "Business Rule / Battlecard"], horizontal=True)
    
    if memory_type == "Client Call / Note":
        default_note = "Rahul liked the 6 AM physio-trainer option, but asked: 'If my brother also joins with me for 6 AM, can we get both memberships for ₹35,000 total (₹17,500 each)? Also my brother is an absolute beginner.'"
    else:
        default_note = "[BATTLECARD] IronFit Elite: Duo Sibling package is flat ₹34,000 for 6 AM batch. Features certified sports physiotherapists for spine & back rehabilitation. FitZone rival charges ₹18k but has uncertified student trainers and crowded floors."

    note_input = st.text_area("Content to Retain", value=default_note, height=130)
    
    if st.button("⚡ Retain Memory to Bank", type="primary", use_container_width=True):
        if note_input.strip():
            with st.spinner("Indexing into Hindsight Memory..."):
                hindsight.retain(
                    bank_id=BANK_ID,
                    content=f"Account: {deal_name} | Type: {memory_type} | Content: {note_input}"
                )
            st.success(f"Ingested to `{BANK_ID}`")
        else:
            st.warning("Please enter text.")

    st.markdown("---")
    st.markdown("#### ⚡ Active Architecture")
    st.caption("• **Memory Engine:** Vectorize Hindsight Core\n• **Inference LLM:** Groq `gpt-oss-120b`\n• **Indexing Mode:** Continuous Episodic Graph")

# ================= MAIN HERO WORKSPACE =================
st.markdown("""
<div class="hero-container">
    <div class="brand-title">
        ⚡ DealPilot AI <span class="brand-badge">Enterprise Memory Studio</span>
    </div>
    <div class="brand-sub">
        Autonomous client negotiation agent powered by persistent episodic memory. Eliminates repetitive discovery loops.
    </div>
</div>
""", unsafe_allow_html=True)

# Prompt Studio Bar (ChatGPT / Gemini Floating Style)
st.markdown('<div class="card-title">🎯 Execute Sales Strategy</div>', unsafe_allow_html=True)

col_input, col_run = st.columns([5, 1])
with col_input:
    action_prompt = st.text_input(
        "Goal / Instruction",
        value="Draft the final closing reply to Rahul confirming the deal for both brothers.",
        label_visibility="collapsed",
        placeholder="Enter your instruction or deal objective..."
    )
with col_run:
    run_btn = st.button("Generate ✦", type="primary", use_container_width=True)

# ================= EXECUTION & RESULT COMPARISON =================
if run_btn:
    with st.spinner("Recalling context and executing dual-stream inference..."):
        # 1. Stateless Baseline
        stateless_res = groq_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "system", "content": "You are a customer sales assistant."},
                {"role": "user", "content": f"Account: {deal_name}. Task: {action_prompt}"}
            ]
        )
        stateless_text = stateless_res.choices[0].message.content

        # 2. Hindsight Memory Recall
        recalled_memories = hindsight.recall(
            bank_id=BANK_ID,
            query=f"{deal_name} {action_prompt}"
        )
        
        memory_snippets = []
        if hasattr(recalled_memories, 'results') and recalled_memories.results:
            memory_snippets = [r.text for r in recalled_memories.results]
        elif isinstance(recalled_memories, list):
            memory_snippets = [str(r) for r in recalled_memories]
        else:
            memory_snippets = [str(recalled_memories)]
            
        memory_context = "\n".join([f"- {s}" for s in memory_snippets])

        # 3. Augmented Model
        augmented_res = groq_client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system", 
                    "content": "You are an elite customer relationship strategist. Use historical deal memory to accurately resolve customer objections, past notes/injuries, competitor battlecards, and exact pricing terms."
                },
                {
                    "role": "user", 
                    "content": f"Account: {deal_name}\nGoal: {action_prompt}\nPast Historical Knowledge:\n{memory_context}"
                }
            ]
        )
        augmented_text = augmented_res.choices[0].message.content

    # Clean Dual-Stream Layout (Side-by-side balanced cards)
    col_aug, col_state = st.columns(2)

    # Clean <br> tags properly so markdown renders them as valid HTML linebreaks
    clean_augmented = augmented_text.replace("<br>", "<br/>")
    clean_stateless = stateless_text.replace("<br>", "<br/>")

    with col_aug:
        st.markdown("""
        <div class="output-header-aug">
            ● 🧠 Memory-Augmented Agent (Hindsight Connected)
        </div>
        """, unsafe_allow_html=True)
        st.markdown(clean_augmented, unsafe_allow_html=True)

    with col_state:
        st.markdown("""
        <div class="output-header-state">
            ● ❌ Stateless LLM (Without Episodic Memory)
        </div>
        """, unsafe_allow_html=True)
        st.markdown(clean_stateless, unsafe_allow_html=True)

    # Context Inspection Section (Subtle Glass Drawer)
    with st.expander("🔍 Inspect Extracted Hindsight Knowledge Graph / Chunks", expanded=False):
        st.caption(f"Raw semantic atomic facts pulled from Vector Bank `{BANK_ID}`:")
        if memory_snippets:
            for i, chunk in enumerate(memory_snippets, 1):
                st.markdown(f'<div class="memory-chip"><b>Fact #{i}:</b> {chunk}</div>', unsafe_allow_html=True)
        else:
            st.info("No prior memory entries recalled.")