from agents import Agent, Runner , ModelSettings, function_tool
from dotenv import load_dotenv
from agents import set_default_openai_key
import asyncio
import os


load_dotenv()
api_key = os.environ.get("OPENAI_API_KEY")
api_model = os.environ.get("OPENAI_MODEL")
set_default_openai_key(api_key)


@function_tool
def get_weather(city: str) -> str:
    """"Get the current weather in a given city"""
    return f"The weather in {city} is sunny with a temperature of 70 degrees."


weather_agent = Agent(
    name="Weather Haiku Agent",
    instructions="You are a weather haiku agent. You are given a city and you need to return a haiku about the weather in that city.",
    tools=[get_weather]
)


result = Runner.run_sync(weather_agent, "What is the weather in Tokyo?")
print(result.final_output)





