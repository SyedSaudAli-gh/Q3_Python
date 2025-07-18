import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
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

async def main():
    agent = Agent(
        name="Assistant",
        instructions="You are a Product Recommendation Agent. Your job is to understand the user's need or problem (such as a symptom or requirement) and recommend a suitable product in response. You must also clearly explain why you are recommending that particular product.",
        model=model
    )

    prompt = "I have a headache"

    result = await Runner.run(agent, prompt, run_config=config)


    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
    