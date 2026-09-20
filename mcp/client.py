from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
load_dotenv()
import sys
import os

import asyncio

async def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    math_server_path = os.path.join(current_dir, "mathserver.py")
    client = MultiServerMCPClient(
        {
            "math": {
                "command":sys.executable, # client then spawns the exact same .venv env
                "args":[math_server_path], ## absolute path
                "transport":"stdio"
            },
            "weather": {
                "url":"http://127.0.0.1:8000/mcp", ## ensure server is running and add /mcp for it to call the mcp tool
                "transport":"streamable_http"
            },
        }
    )

    model_name = os.getenv("OLLAMA_MODEL")

    tools = await client.get_tools()
    model = ChatOllama(model=model_name)
    agent = create_agent(model,tools)
    math_response = await agent.ainvoke({"messages": [{"role": 'user', "content": "What's (3+5) x 12?"}]})
    
    print("Math Respnse:", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke({"messages": [{"role": 'user', "content": "What's the weather in Bengaluru?"}]})
    
    print("weather Respnse:", weather_response["messages"][-1].content)

asyncio.run(main())