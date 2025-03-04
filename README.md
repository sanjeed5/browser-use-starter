# Browser-Use Starter

A starter project for browser automation using the Browser-Use framework.

## Setup

1. Clone this repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
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

### Agent Configuration
- `AGENT_CONFIG`: Settings for the agent (vision, planning interval, logs)
- `SENSITIVE_DATA`: Credentials and sensitive information
- `DEFAULT_TASK`: The default task for the agent to perform

## Running the Agent

To run the agent with your configuration:

```bash
python agent.py
```

## Examples

To change the default task, edit the `DEFAULT_TASK` variable in `config.py`:

```python
DEFAULT_TASK = "Search for flights from New York to London on March 15, 2025."
```

To use a different browser, update the `LOCAL_BROWSER_CONFIG`:

```python
LOCAL_BROWSER_CONFIG = {
    "chrome_instance_path": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
}
```

## Logs

Logs are saved in the `logs/` directory:
- Conversation logs: `logs/conversation`
- History summary: `logs/history_summary.json`
