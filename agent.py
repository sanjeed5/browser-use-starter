from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent, BrowserConfig, Browser, Controller, ActionResult
import asyncio
import json
import os
from config import (
    GOOGLE_API_KEY,
    LLM_CONFIG,
    PLANNER_LLM_CONFIG,
    BROWSER_CONFIG,
    LOCAL_BROWSER_CONFIG,
    AGENT_CONFIG,
    SENSITIVE_DATA,
    DEFAULT_TASK
)

# Initialize LLMs with configuration
llm = ChatGoogleGenerativeAI(
    model=LLM_CONFIG["model"],
    max_retries=LLM_CONFIG["max_retries"],
    google_api_key=GOOGLE_API_KEY
)

planner_llm = ChatGoogleGenerativeAI(
    model=PLANNER_LLM_CONFIG["model"], 
    max_retries=PLANNER_LLM_CONFIG["max_retries"],
    google_api_key=GOOGLE_API_KEY
)

# Basic configuration
browser_config = BrowserConfig(
    headless=BROWSER_CONFIG["headless"],
    disable_security=BROWSER_CONFIG["disable_security"]
)

# Local browser configuration
local_browser = Browser(config=BrowserConfig(
    chrome_instance_path=f"`{LOCAL_BROWSER_CONFIG['chrome_instance_path']}`"
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
        task=DEFAULT_TASK,
        llm=llm,
        save_conversation_path=AGENT_CONFIG["save_conversation_path"],
        planner_llm=planner_llm,
        use_vision_for_planner=AGENT_CONFIG["use_vision_for_planner"],
        planner_interval=AGENT_CONFIG["planner_interval"],
        sensitive_data=SENSITIVE_DATA,
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


if __name__ == "__main__":
    asyncio.run(main())
