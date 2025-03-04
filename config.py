"""
Configuration file for Browser-Use project.
Edit this file to customize your browser automation settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# LLM Configuration
LLM_CONFIG = {
    "model": "gemini-2.0-flash-lite",
    "max_retries": 10,
}

PLANNER_LLM_CONFIG = {
    "model": "gemini-2.0-flash",
    "max_retries": 10,
}

# Browser Configuration
BROWSER_CONFIG = {
    "headless": False,
    "disable_security": True,
}

# Local Browser Configuration (for using a local browser instance)
LOCAL_BROWSER_CONFIG = {
    "chrome_instance_path": "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    # Add any other local browser settings here
}

# Toggle to use local browser instead of the default browser
# Set to True to use your local browser with saved cookies/sessions
# Set to False to use a clean browser instance
USE_LOCAL_BROWSER = False

# Agent Configuration
AGENT_CONFIG = {
    "use_vision_for_planner": False,
    "planner_interval": 10,
    "save_conversation_path": "logs/conversation",
}

# Sensitive Data (credentials, etc.)
# Note: In production, consider using a more secure method to store credentials
SENSITIVE_DATA = {
    "x_name": "magnus",
    "x_password": "12345678",
}

# Task Configuration
DEFAULT_TASK = "Search for the weather forecast for New York City for the next 3 days and summarize it."

# Alternative tasks you can try (uncomment to use)
ALTERNATIVE_TASKS = [
    # "Find the top 5 most popular movies currently showing and create a list with their ratings.",
    # "Search for a simple chocolate chip cookie recipe and save the ingredients list.",
    # "Look up the current price of Apple stock and its performance over the past week.",
    # "Find the latest news headlines about artificial intelligence and summarize the top 3 stories.",
    # "Search for flights from New York to London for next month and find the cheapest option.",
] 