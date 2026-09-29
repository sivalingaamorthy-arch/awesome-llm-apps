# Frameworks, Ecosystems, and Tools Used in `awesome-llm-apps`

This repository is a curated collection of AI agents, agent frameworks, RAG pipelines, and LLM-powered apps. It brings together multiple ecosystems instead of relying on a single stack.

## 1) AI Agent Frameworks

These are the main frameworks used to build and orchestrate agents.

| Framework | Purpose | Notes |
|---|---|---|
| Google ADK (Agent Development Kit) | Agent orchestration and tooling | Used in crash-course examples and tool-using agents |
| OpenAI Agents SDK | Agent runtime and orchestration | Used for function calling, handoffs, tool use, evaluations |
| LangGraph | Workflow and stateful agent patterns | Popular for agentic RAG and graph-based orchestration |
| CrewAI | Multi-agent team workflows | Used for agency-style teams and collaborative agents |
| Agno | Lightweight agent and tool framework | Used in several AI apps and research tools |
| AG2 / AutoGen-style multi-agent patterns | Agent collaboration and routing | Used in adaptive research and team workflows |
| PydanticAI | Type-safe AI application development | Used for validated outputs and structured AI apps |
| EvoAgentX | Self-evolving workflows | Used in self-improving agent examples |

## 2) LLM Providers and Model Ecosystem

This repo spans multiple model providers and local/open-source model stacks.

| Provider / Model Ecosystem | Typical Use |
|---|---|
| OpenAI (GPT-4o, GPT-4, GPT-3.5) | General reasoning, research agents, chat tools |
| Google Gemini | Multimodal reasoning, voice, UI agents |
| Anthropic Claude | Agent reasoning and orchestration |
| DeepSeek | Long reasoning and architecture/agent workflows |
| Llama 3.x / 3.1 / 3.2 | Local LLM and RAG use cases |
| Qwen | Open-source model experimentation |
| Cohere | Retrieval and RAG integrations |
| Together AI | Hosted access to multiple open-source models |
| xAI Grok | Finance and domain-specific agents |
| Ollama / local models | Fully local execution, privacy-friendly demos |
| Phi4, Gemma 3, Mistral | Smaller/local open-source model examples |

## 3) RAG and Retrieval Ecosystem

The repo heavily emphasizes retrieval-augmented generation and knowledge-grounded AI applications.

| Tool / Component | Purpose |
|---|---|
| Qdrant | Vector search and memory storage |
| Pinecone | Managed vector database examples |
| ChromaDB | Embedding and document storage |
| Weaviate | Vector search and knowledge retrieval |
| Milvus | High-scale vector database |
| LangChain | Retrieval and tool integration |
| LlamaIndex | Agentic and document-based retrieval |
| Mem0 | Memory layer for persistent conversation memory |
| Redis | Session/memory backend |
| Embedding models | Search and semantic retrieval |

## 4) Frontend and App UI Layers

Several projects expose user interfaces through browser-based apps and dashboards.

| Stack | Purpose |
|---|---|
| Streamlit | Fast AI app UI and prototypes |
| FastAPI | API backend for AI apps |
| Flask | Lightweight app server |
| Next.js | Modern frontend UI for agentic apps |
| React | Component-based web interfaces |
| TailwindCSS | Styling framework for responsive AI dashboards |
| Plotly | Interactive dashboards and charts |
| react-force-graph-2d | Graph visualization for knowledge graphs |

## 5) Browser, Web, and Search Automation

These tools help agents browse the web, scrape pages, and interact with online content.

| Tool | Purpose |
|---|---|
| Playwright | Browser automation and real web interaction |
| Browser Use | AI-assisted browser control |
| Firecrawl | Search and crawl the web programmatically |
| DuckDuckGo Search | Privacy-first web search |
| Wikipedia API | Structured knowledge retrieval |
| ArXiv API | Academic research retrieval |
| Yahoo Finance API | Financial data lookup |
| Google Maps / Airbnb APIs | Travel and location-based intelligence |
| BeautifulSoup | HTML scraping |
| Scrapy | Large-scale scraping frameworks |

## 6) Voice, Speech, and Audio Processing

The repo includes voice agents and audio-driven intelligence.

| Tool | Purpose |
|---|---|
| Faster-Whisper | Speech-to-text |
| Whisper | Transcription and audio understanding |
| Librosa | Audio feature analysis |
| Gemini 3.8 Live | Real-time voice AI |
| ElevenLabs | Text-to-speech generation |
| Google TTS | Voice synthesis |
| Deepgram | Voice transcription services |

## 7) Vision, Image, and Multimodal AI

These tools support image, video, and multimodal understanding.

| Tool | Purpose |
|---|---|
| OpenCV | Computer vision and image processing |
| DeepFace | Facial recognition and emotion analysis |
| MediaPipe | ML pipelines for vision and motion tracking |
| MoviePy | Video editing and processing |
| Pillow / PIL | Graphics and image manipulation |
| Gemini Vision | Visual reasoning |
| Embed-4 / multimodal embeddings | Vision-based retrieval and understanding |

## 8) MCP and Tool Integration Ecosystem

The repo includes examples of standardized tool integration via MCP.

| Technology | Purpose |
|---|---|
| Model Context Protocol (MCP) | Standard interface for tools and context |
| LangChain Tools | Web search, Wikipedia, and external tools |
| CrewAI Tools | File reading, web scraping, directory search |
| Function Calling | Direct tool invocation by LLMs |

## 9) Memory and Personalization

These patterns help apps remember context and personalize interactions.

| Tool | Purpose |
|---|---|
| Mem0 | Persistent memory for agents |
| Redis | Session state / memory backend |
| Local chat memory patterns | Personalized AI assistants |

## 10) Fine-Tuning and Optimization

The repo includes model optimization and training patterns.

| Tool | Purpose |
|---|---|
| LoRA | Efficient fine-tuning |
| Unsloth | Fast fine-tuning workflows |
| Headroom | Context token optimization |
| TOON Format | Prompt/token optimization |
| Transformers / Hugging Face | Open-source model training and inference |

## 11) Development and Deployment Infrastructure

| Tool | Purpose |
|---|---|
| Docker | Containerization |
| Ollama | Local LLM deployment |
| GitHub | Repo hosting and project management |
| OpenRouter | Multi-provider model routing |
| Colab | Cloud notebooks for experimentation |

## 12) Notable Examples of Ecosystem Usage in This Repo

Based on the project structure and README, the repo combines these ecosystems together:

- **Agent frameworks:** Google ADK, OpenAI Agents SDK, LangGraph, CrewAI, Agno
- **Model access:** OpenAI, Gemini, Claude, DeepSeek, Llama, Qwen, Mistral
- **UI stacks:** Streamlit, FastAPI, Next.js, React, TailwindCSS
- **Retrieval:** Qdrant, Pinecone, ChromaDB, Weaviate, LangChain, LlamaIndex
- **Browser tools:** Playwright, Firecrawl, BrowserUse
- **Voice:** Whisper, Faster-Whisper, Gemini Live, Deepgram
- **Vision:** OpenCV, MediaPipe, DeepFace, Gemini Vision
- **Protocols:** MCP, function calling, tool use APIs

## 13) Language Composition

The repository uses multiple languages optimized for different tasks:

| Language | Percentage | Primary Use |
|---|---|---|
| Python | 55.1% | AI logic, agents, backends, data processing |
| TypeScript | 19.6% | Frontend frameworks, type-safe web apps |
| JavaScript | 17.9% | Browser interactions, frontend utilities |
| HTML | 4.4% | Web templates and structure |
| CSS | 2.8% | Styling and UI design |
| Dockerfile | 0.1% | Container deployment |
| Other | 0.1% | Configuration and miscellaneous |

## 14) Overall Summary

This repository is not tied to a single framework. Instead, it acts as a broad ecosystem map for modern AI application development:

- **Python** is the dominant language for AI and agent logic.
- **Agent orchestration** is spread across ADK, OpenAI Agents SDK, LangGraph, CrewAI, and Agno.
- **Apps** are built with Streamlit, FastAPI, Next.js, and React.
- **Retrieval and memory** layers rely on vector DBs and memory tools.
- **Browser automation, voice, and vision** systems add multimodal capabilities.
- **Models** span proprietary (OpenAI, Google, Anthropic) and open-source (Llama, Qwen, Mistral).

This makes `awesome-llm-apps` a practical showcase of how different AI stacks fit together in real-world LLM app development.

---

**Last Updated:** 2026-09-29  
**Repository:** [awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
