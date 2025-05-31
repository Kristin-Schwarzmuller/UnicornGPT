# UnicornGPT

A fun, kid-friendly AI assistant created for a birthday party that lets children interact with whimsical characters. Simply choose a character, ask questions, and get entertaining responses. The project includes family-specific Easter eggs for personalized fun.

## Features

- 🎭 Interactive AI characters with unique personalities
- 🗣️ Speech-to-text and text-to-speech capabilities
- 🦄 Whimsical, kid-friendly responses
- 🥳 Hidden Easter eggs for personalized fun
- 🚀 Supports both Azure and local LLM options

## Requirements

- Python 3.12.4 (recommended)
- Vosk speech recognition model
- Either:
  - Azure AI account (for cloud-based LLM)
  - Ollama (for local LLM)

## Installation

### 1. Create a virtual environment and install dependencies

Recommended python version: 3.12.4

```bash
# Create virtual environment
python -m venv .venv

# Activate the environment
# Windows:
.venv\Scripts\activate
# Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Download a speech recognition model

Download vosk language model from https://alphacephei.com/vosk/models and place in `./data/models/`  
Recommendation: `vosk-model-en-us-0.42-gigaspeech`

### 3. Configure your LLM

#### Option A: Azure

If you want to use Azure Language Models:
1. Go to Azure AI Studio (https://ai.azure.com) and deploy a language model
2. Recommendation: Ministral-3B
3. Save the API key and endpoint in a `.env` file in the root folder:

```
AZURE_API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
AZURE_ENDPOINT="https://<your-model>.services.ai.azure.com/models"
```

#### Option B: Ollama

If you want to use your local LLM:
1. Make sure you have Ollama installed
2. Pull the recommended model: `llama3:latest`

## Usage

When starting the program:
1. Choose a character when prompted
2. The AI will select a random candy and voice
3. Ask questions by starting with the character name
4. End your question with "please" to indicate you're done speaking
5. Wait for the AI's response

Example:
```
Turtle, how much cake should I eat today, please?
```

Note: Azure responses are typically faster than Ollama.