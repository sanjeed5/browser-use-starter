from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    max_retries=5,
)

async def main():
    agent = Agent(
        task="Go to google.com, search for trains from Mangalore to Bangalore on 22nd feb 2025.",
        llm=llm,
    )
    result = await agent.run()
    print(result)


asyncio.run(main())
