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
    "model": "gemini-2.0-flash",
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
    "chrome_instance_path": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    # Brave Browser path (if needed in the future):
    # "chrome_instance_path": "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
    # Add any other local browser settings here
}

# Toggle to use local browser instead of the default browser
# Set to True to use your local browser with saved cookies/sessions
# Set to False to use a clean browser instance
USE_LOCAL_BROWSER = True

# Agent Configuration
AGENT_CONFIG = {
    "use_vision_for_planner": False,
    "planner_interval": 5,
    "save_conversation_path": "logs/conversation",
}

# Initial actions to run without LLM
# These actions will be executed in sequence before the LLM takes control
# See: https://docs.browser-use.com/customize/agent-settings#run-initial-actions-without-llm
# This feature allows you to automate repetitive initial steps without using the LLM,
# which can save time and tokens, and make the automation more reliable.
INITIAL_ACTIONS = [
    {'open_tab': {'url': 'https://www.producthunt.com/posts/new'}},
]

"""
Example of more complex initial actions:

INITIAL_ACTIONS = [
    # Basic navigation
    {'open_tab': {'url': 'https://www.producthunt.com/posts/new'}},
    {'wait': {'seconds': 3}},  # Wait for page to load
    
    # Form interactions
    {'input_text': {'index': 1, 'text': 'https://github.com/sanjeed5/new-mac-setup'}},
    {'input_text': {'index': 2, 'text': 'Mac Development Setup CLI'}},
    
    # Dropdown interactions
    {'get_dropdown_options': {'index': 3}},  # Get available options first
    {'select_dropdown_option': {'index': 3, 'text': 'Developer Tools'}},
    
    # Scrolling
    {'scroll_down': {'amount': 500}},
    {'scroll_to_text': {'text': 'Comments'}},
    
    # Special key interactions
    {'send_keys': {'keys': 'Enter'}},
    {'send_keys': {'keys': 'Control+s'}},
    
    # Multiple tabs
    {'open_tab': {'url': 'https://github.com/sanjeed5/new-mac-setup'}},
    {'switch_tab': {'page_id': 0}},
    
    # Content extraction
    {'extract_content': {'goal': 'Find all company names mentioned on the page'}},
    
    # Navigation controls
    {'go_back': {}},
    {'search_google': {'query': 'Mac Development Setup CLI github'}}
]
"""

# Sensitive Data (credentials, etc.)
# Note: In production, consider using a more secure method to store credentials
SENSITIVE_DATA = {
    # "x_name": "magnus",
    # "x_password": "12345678",
}

# Task Configuration
DEFAULT_TASK = """Create a product hunt launch post and complete it. Ask human for input if you're stuck or need clarification. Wait for human input when you need to upload any media files. You can use this as a video link if possible, https://asciinema.org/a/706283, ignore if errors. 

1. Product Hunt Launch Post
URL: https://github.com/sanjeed5/new-mac-setup
Name of the product: Mac Development Setup CLI
Tagline: Automate your Mac dev environment setup in minutes, not days.
Topics: Developer Tools, Productivity, Open Source
Pricing tag: Free
Status: Available
Description:
Mac Development Setup is an open-source toolkit that automates the setup of a new Mac for development. It handles everything from installing Homebrew packages to configuring your shell, development tools, and macOS preferences - all while keeping your sensitive data secure.
Gallery: 
- Use demo.gif and thumbnail.png from the mentioned folder
First Comment:
Hey Product Hunt! 👋
I created Mac Development Setup because I was tired of wasting an entire day configuring a new Mac when I could be doing actual work. This toolkit automates everything I need for a productive development environment - from Homebrew packages to shell configuration, Node.js, Python, Git setup, and more.
What makes this different:
Modular design: Install only what you need
Security-focused: Clear separation between public and private data
Comprehensive: Handles everything from dev tools to macOS preferences
I'd love to hear what you think and what other features would be useful! What's your biggest pain point when setting up a new development machine?

"""

# Alternative tasks you can try (uncomment to use)
ALTERNATIVE_TASKS = [
    # "Find the top 5 most popular movies currently showing and create a list with their ratings.",
    # "Search for a simple chocolate chip cookie recipe and save the ingredients list.",
    # "Look up the current price of Apple stock and its performance over the past week.",
    # "Find the latest news headlines about artificial intelligence and summarize the top 3 stories.",
    # "Search for flights from New York to London for next month and find the cheapest option.",
] 