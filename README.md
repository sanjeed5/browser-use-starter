# Browser-Use Starter

A starter project for browser automation using the Browser-Use framework.

## Setup

1. Clone this repository
2. Create a virtual environment using uv:
   ```bash
   uv venv --python 3.11
   ```
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies using uv:
   ```bash
   uv sync
   ```
5. Copy `.env.example` to `.env` and add your API keys

## Configuration

This project uses a centralized configuration system in `config.py`. You can customize the following settings:

### API Keys
- `GOOGLE_API_KEY`: Your Google API key for Gemini models

### LLM Configuration
- `LLM_CONFIG`: Settings for the main language model
- `PLANNER_LLM_CONFIG`: Settings for the planner language model

### Browser Configuration
- `BROWSER_CONFIG`: General browser settings (headless mode, security settings)
- `LOCAL_BROWSER_CONFIG`: Settings for using a local browser instance
- `USE_LOCAL_BROWSER`: Toggle between using your local browser (with saved cookies/sessions) or a clean browser instance

### Agent Configuration
- `AGENT_CONFIG`: Settings for the agent (vision, planning interval, logs)
- `SENSITIVE_DATA`: Credentials and sensitive information
- `DEFAULT_TASK`: The default task for the agent to perform

## Running the Agent

To run the agent with your configuration:

```bash
uv run agent.py
```

## Adding New Dependencies

To add a new package to your project:

```bash
uv add <package-name>
```

## Examples

To change the default task, edit the `DEFAULT_TASK` variable in `config.py`:

```python
DEFAULT_TASK = "Search for flights from New York to London on March 15, 2025."
```

To use your local browser with saved cookies and sessions, set:

```python
USE_LOCAL_BROWSER = True
LOCAL_BROWSER_CONFIG = {
    "chrome_instance_path": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
}
```

## Logs

Logs are saved in the `logs/` directory:
- Conversation logs: `logs/conversation`
- History summary: `logs/history_summary.json`
