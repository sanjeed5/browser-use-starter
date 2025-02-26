from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, BrowserConfig, Browser, Controller, ActionResult
import asyncio
from dotenv import load_dotenv
import json
import os
load_dotenv()
from browser_use import BrowserConfig

sensitive_data = {'x_name': 'magnus', 'x_password': '12345678'}

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    max_retries=10,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
planner_llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash', 
    max_retries=10,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Basic configuration
browser_config = BrowserConfig(
    headless=False,
    disable_security=True
)

local_browser = Browser(config=BrowserConfig(
    chrome_instance_path="`/Applications/Brave Browser.app/Contents/MacOS/Brave Browser`"
))

browser = Browser(config=browser_config)

# Initialize the controller
controller = Controller()

@controller.action('Ask user for information')
def ask_human(question: str) -> str:
    answer = input(f'\n{question}\nInput: ')
    return ActionResult(extracted_content=answer)

async def main():
    agent = Agent(
        browser=browser,
        task="Search for trains from Mangalore to Bangalore on 22nd feb 2025.",
        llm=llm,
        save_conversation_path="logs/conversation",  # Save chat logs
        planner_llm=planner_llm,           # Separate model for planning
        use_vision_for_planner=False,      # Disable vision for planner
        planner_interval=10,                # Plan every 10 steps
        sensitive_data=sensitive_data,     # The model will only see the keys (x_name, x_password) but never the actual values
        controller=controller
    )
    history = await agent.run()
    
    # Print the final result and full history
    print(history.final_result())
    print("--------------------------------")
    print(history)
    
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    # Save useful information from the history to a JSON file
    history_data = {
        "final_result": history.final_result(),
        "is_done": history.is_done(),
        "has_errors": history.has_errors(),
        "errors": history.errors(),
        "urls_visited": history.urls(),
        "screenshots": history.screenshots(),
        "action_names": history.action_names(),
        "extracted_content": history.extracted_content(),
        "model_actions": history.model_actions()
    }
    
    with open("logs/history_summary.json", "w") as f:
        json.dump(history_data, f, indent=2)


asyncio.run(main())
