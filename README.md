# BMO

> A desktop AI companion inspired by BMO from *Adventure Time*. Built entirely in Python, featuring desktop animations, persistent memory, real-time weather integration, and local LLM-powered conversations.

## Features

- **Animated Desktop Companion**
  - Custom hand-drawn BMO sprite
  - Frame-by-frame idle animations
  - Transparent always-on-top window

- **Local AI Conversations**
  - Powered by Ollama and LLaMA 3.2
  - Natural language interactions
  - In-character dialogue

- **Persistent Memory**
  - Remembers user information
  - Stores conversation history locally
  - JSON-based memory system


## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core application |
| Tkinter | Desktop UI |
| Pillow | Sprite rendering |
| Ollama | Local LLM runtime |
| LLaMA 3.2 | Conversational AI |
| Open-Meteo | Weather API |
| JSON | Memory persistence |

## How It Works

1. Launch BMO.
2. Click on BMO to open the chat interface.
3. Send a message.
4. Receive an AI-generated response.
5. BMO remembers previous conversations for future sessions.

## Installation

```bash
git clone https://github.com/leya00/BMO.git
cd BMO
pip install -r requirements.txt
ollama pull llama3.2
python main.py
```

## Requirements

- Python 3.10+
- Ollama installed
- LLaMA 3.2 model downloaded

## Roadmap

- [ ] Voice input
- [ ] Text-to-speech
- [ ] Additional animations
- [ ] Improved memory system
- [ ] Custom personalities
