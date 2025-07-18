import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
import asyncio

# Load the environment variables from the .env file
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

#Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

@function_tool
def get_country_info(country: str, capital: str) -> str:
    """
    Get information about a capital of a country.
    """
    return f"{country} is a country with its capital is {capital}. It is known for its rich culture and history. The capital city, {capital}."

@function_tool
def get_language(country: str) -> str:
    """
    Return the official language(s) of the given country.
    """
    country = country.lower()
    if country == "pakistan":
        return "Urdu"
    elif country == "france":
        return "French"
    elif country == "japan":
        return "Japanese"
    else:
        return "Language information not available."

@function_tool
def country_population(country: str, population:int) -> str:
    """
    Get the population of a country.
    """
    return f"The population of {country} is approximately {population} million people."

async def main():
    agent = Agent(
    name="Assistant",
    instructions="""
    You are a helpful assistant that can provide:
    - Information about a country's capital using the get_country_info tool.
    - Translations of text using the language_translation tool.
    - Population details using the country_population tool.

    Decide which tool to use based on the user's message. Always call the appropriate tool to answer.
    """,
    model=model,
    tools=[get_country_info, get_language, country_population]
)


    prompt = "what is the language of france?. Also, tell me about its capital and population."

    result = await Runner.run(agent, prompt, run_config=config)


    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
    