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
