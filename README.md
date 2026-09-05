# Trend-Spotter 

Trend-Spotter is a CrewAI-powered trend spotting newsletter generator. It uses a team of specialized AI agents to research, analyze, and write a high-engagement newsletter based on any niche you provide.

##  The Crew

The project utilizes three specialized agents:
1. **Trend Researcher**: Scans digital signals (Reddit, X, blogs, GitHub) to identify emerging trends.
2. **Market Analyst**: Evaluates the trends to separate hype from value and assigns impact scores.
3. **Newsletter Editor**: Synthesizes the analysis into a punchy, reader-friendly newsletter.

## ️ Setup

### Prerequisites
- Python 3.10 - 3.12
- A Serper.dev API key (for web search capabilities)

### Installation
1. Clone the repository.
2. Navigate to the project directory:
   ```bash
   cd project_root
   ```
3. Install dependencies:
   ```bash
   uv sync
   ```

### Configuration
1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
2. Open `.env` and replace `your_serper_api_key_here` with your actual Serper.dev API key.

##  Running the App

You can run the newsletter generator by specifying a niche as an argument:

```bash
uv run trend-spotter "AI in Healthcare"
```

Alternatively, run it without arguments and the app will prompt you for the niche:

```bash
uv run trend-spotter
```

The resulting newsletter will be saved as a `.txt` file in the current directory.

##  Project Structure
- `agents.py`: Definition of the AI agents.
- `tasks.py`: Definition of the tasks assigned to each agent.
- `crew.py`: Orchestration logic to assemble agents and tasks into a Crew.
- `main.py`: Application entry point.
- `pyproject.toml`: Project metadata and dependencies.
"# Trend-Spotter" 
