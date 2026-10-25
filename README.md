# Google Search Agent

A lightweight AI-powered research assistant built with Python, LangGraph, and FastAPI. It uses a Groq LLM and Google Serper web search to answer user questions with up-to-date information.

## Overview

This project consists of:

- `agent.py` — defines the LangGraph agent and the Google search tool
- `fast_api_server.py` — exposes the agent through a FastAPI HTTP API
- `langgraph.json` — LangGraph configuration for graph deployment/runtime wiring
- `requirements.txt` — project dependencies

## Features

- Google Search integration via Serper API
- LLM-powered reasoning through Groq
- FastAPI endpoints for health checks and search requests
- Graph-based agent structure compatible with LangGraph

## Project structure

```text
Google-Search-Agent/
├── agent.py
├── fast_api_server.py
├── langgraph.json
├── requirements.txt
├── .env.example (optional local file you create)
└── README.md
```

## Prerequisites

- Python 3.10+
- A valid `SERPER_API_KEY`
- A valid `GROQ_API_KEY`

## Setup

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with:

```env
SERPER_API_KEY=your_serper_api_key
GROQ_API_KEY=your_groq_api_key
```

## Run the app

Start the FastAPI server:

```bash
uvicorn fast_api_server:app --reload --host 0.0.0.0 --port 8000
```

The app will be available at:

- `http://localhost:8000/health`
- `http://localhost:8000/docs`

## API usage

### Health check

```bash
curl http://localhost:8000/health
```

### Search endpoint

```bash
curl -X POST http://localhost:8000/search \
  -H "Content-Type: application/json" \
  -d '{"query":"What are the latest trends in AI agents?"}'
```

Example response:

```json
{
  "query": "What are the latest trends in AI agents?",
  "answer": "...model-generated response..."
}
```

## Notes

- The agent is defined in `agent.py` and is imported into `fast_api_server.py`.
- The search tool uses `GoogleSerperAPIWrapper` to fetch current web results.
- The LLM model is configured to `openai/gpt-oss-120b` via `ChatGroq`.
- The project is intentionally simple and can be extended with more tools, memory, or advanced routing.

 
