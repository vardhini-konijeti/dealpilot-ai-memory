# ⚡ DealPilot AI — Enterprise Memory Studio

DealPilot is an autonomous deal negotiation copilot powered by persistent episodic memory. Unlike standard stateless AI agents that may make unauthorized concessions or generate generic responses, DealPilot retains historical client objections, company financial boundaries, and competitor battlecards to support high-value enterprise deal negotiations.

Built with **Vectorize Hindsight** and **Groq (gpt-oss-120b)**.

## 🚀 Key Features

- **Persistent Episodic Memory:** Ingests discovery calls, client constraints, and pricing limits across multi-week deal cycles using [Vectorize Hindsight](https://github.com/vectorize-io/hindsight).
- **Policy Guardrails & Firm Negotiation:** Rejects unauthorized concessions, such as risky 60-day post-payment terms, and proposes approved alternatives such as escrow milestones and rollback guarantees.
- **Dual-Stream Comparative Studio:** Provides live side-by-side evaluation between standard stateless LLMs and memory-augmented agents.
- **Inspectable Semantic Knowledge Graph:** Enables direct inspection of atomic facts and entity relationships extracted into Hindsight memory banks.

## 🛠️ Tech Stack

- **Memory Engine:** [Hindsight by Vectorize](https://hindsight.vectorize.io/)
- **Inference LLM:** Groq (`openai/gpt-oss-120b`)
- **Frontend / Studio:** Streamlit with a custom glassmorphism dark UI

## 📦 Setup & Installation

### 1. Clone the Repository

Clone the project repository and navigate to the project directory:

```
git clone https://github.com/<YOUR_GITHUB_USERNAME>/dealpilot-ai-memory.git
cd dealpilot-ai-memory
```

Replace `<YOUR_GITHUB_USERNAME>` with your actual GitHub username.

### 2. Install Dependencies

Install all required Python dependencies:

```
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory of the project and add the following variables:

```
GROQ_API_KEY=your_groq_api_key_here
HINDSIGHT_API_KEY=your_hindsight_api_key_here
HINDSIGHT_BASE_URL=https://api.hindsight.vectorize.io
```

> **Important:** Never commit or upload your `.env` file to GitHub because it contains sensitive API keys. Make sure `.env` is included in your `.gitignore` file.

### 4. Launch the Studio

Start the Streamlit application:

```
streamlit run app.py
```

After running the command, Streamlit will provide a local URL. Open that URL in your browser to access the DealPilot AI Enterprise Memory Studio.

---

