# 🤖 Fine-tuned with Whatsapp Group Chat AI Bot

A personalized, "funny" WhatsApp chatbot fine-tuned on group chat history. This project uses **Small Language Models (SLMs)** to capture the specific humor, inside jokes, and slang of your friend group while running efficiently on local consumer hardware.

## 📁 Project Structure

```text
harddevs-bot/
├── training/                # SLM Fine-tuning (Cloud/Colab focused)
│   ├── scripts/             # Data processing scripts
│   ├── data/                # Raw and cleaned datasets (Git ignored)
│   └── train.ipynb          # Main Unsloth training notebook
├── local_bot/               # WhatsApp Bridge (Local/WSL)
│   ├── index.js             # Node.js entry point
│   ├── Modelfile            # Ollama configuration
│   └── package.json         # Node.js dependencies
├── models/                  # Storage for exported GGUF weights
└── README.md                # You are here
```

## 🛠️ Prerequisites
1. Python Environment (Training)
- **Version**: Python 3.12 or higher.
- **Manager (Recommended)**: uv (Extremely fast Rust-based manager) or standard venv.
  - To install uv: curl -LsSf https://astral.sh/uv/install.sh | sh (Unix) or via PowerShell on Windows.
- **Cloud**: Designed for Google Colab using A100 or L4 GPUs to handle fine-tuning in under 15 minutes.

2. Node.js Environment (Local Bot)
- **Version**: Node.js 24 LTS.
- **OS**: WSL2 (Ubuntu 24.04 recommended), Linux, or macOS.
- **Key Dependencies**: `whatsapp-web.js` (uses Puppeteer for browser emulation).

3. AI Engine (Inference)
- **Ollama**: The engine for running your local "Brain."
- **Windows**: Download the official installer from ollama.com.
- **Linux/WSL**: `curl -fsSL https://ollama.com/install.sh | sh`.
