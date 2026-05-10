# 🤖 CrewAI Learning Project — AMD Developer Hackathon

This project was developed as a learning journey into **AI Agents** using [CrewAI](https://crewai.com), built during the **AMD Developer Hackathon** hosted on [lablab.ai](https://lablab.ai).

The goal was never to ship a polished product, but to **understand how to build, configure and run AI agent crews from scratch** — going from zero knowledge to a functional multi-agent research pipeline.

Also published on Hugging Face: `<!-- ADD HUGGING FACE LINK HERE -->`

---

## 📁 Project Structure

```
crewai/
├── first-crewai/         # "Hello World" of CrewAI — first contact with the framework
├── research_crew/        # Manual version — built by hand following the docs, without CLI
└── research_crew_v2/     # ✅ Functional version — created with the CrewAI CLI
```

---

## 🧠 What Each Version Represents

### `first-crewai`
The very first contact with CrewAI. Not a real crew — just a minimal setup to understand how the framework works, how to install it with `uv`, and how the basic structure looks.

### `research_crew`
A manual attempt at building a crew without using the `crewai create` CLI command. Built by hand following the official documentation. Faced several structural issues (missing `pyproject.toml`, wrong module paths, entrypoint configuration) that were resolved through trial and error. A valuable learning experience.

### `research_crew_v2` ✅
The functional version. Generated with `uvx crewai create crew research-crew-v2` and customized with:
- Agents and tasks translated to Portuguese
- Topic focused on **Edge Computing, Embedded Systems, IoT with ESP32, and Cloud Platforms (AWS, GCP, Azure)**
- LLM powered by **Groq API** (`llama-3.3-70b-versatile`)
- Web search tool powered by **Serper**

---

## 🚀 How It Works

The `research_crew_v2` runs a sequential two-agent pipeline:

```
researcher agent
    └── Searches the web and gathers information about the topic
            ↓
reporting_analyst agent
    └── Analyzes the research and produces a structured report (report.md)
```

Both agents are configured via YAML files (`agents.yaml`, `tasks.yaml`) and powered by a Groq-hosted LLaMA model.

---

## 🛠️ Tech Stack

| Tool | Role |
|---|---|
| [CrewAI](https://crewai.com) | Multi-agent framework |
| [Groq](https://groq.com) | LLM inference (LLaMA 3.3 70B) |
| [Serper](https://serper.dev) | Web search tool for agents |
| [uv](https://astral.sh/uv) | Python package and environment manager |
| Python 3.13 | Language |

---

## ⚙️ Setup & Running

### Prerequisites
- Python 3.13+
- `uv` installed
- Groq API key — [groq.com](https://groq.com)
- Serper API key — [serper.dev](https://serper.dev)

### Steps

```bash
# Clone the repo and navigate to the functional version
cd research_crew_v2

# Install dependencies
uv run crewai install

# Create your .env file
cp .env.example .env
# Fill in your GROQ_API_KEY, SERPER_API_KEY and MODEL
```

**.env**
```env
GROQ_API_KEY=your_groq_key
SERPER_API_KEY=your_serper_key
MODEL=groq/llama-3.3-70b-versatile
```

```bash
# Run the crew
uv run crewai run
```

The output report will be saved to `report.md`.

---

## 📄 Sample Output

The crew generates a comprehensive research report in Portuguese covering:
- Key concepts and definitions
- Historical development and recent trends
- Main challenges and opportunities
- Relevant applications and case studies
- Future perspectives

---

## 👨‍💻 Author

**Rafael Varela**
Built during the AMD Developer Hackathon on lablab.ai — May 2026.
