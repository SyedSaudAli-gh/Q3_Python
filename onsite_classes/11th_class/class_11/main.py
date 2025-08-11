import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, RunContextWrapper 
from agents.run import RunConfig
from pydantic import BaseModel
# from run_context_wrapper import RunContextWrapper

# Load environment variables
load_dotenv()

# Get Gemini API key from environment
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Setup external client for Gemini
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Setup model and run configuration
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define context schema
class AgeContext(BaseModel):
    age: int
    name: str

# Tool function
@function_tool
async def check_age(wrapper: RunContextWrapper[AgeContext]) -> str:
    """
    Check if the user is an adult or a minor based on the age provided.
    """
    age = wrapper.context.age
    name = wrapper.context.name
    if age >= 18:
        return f"{name} is an adult."
    else:
        return f"{name} is a minor."

# Main async runner
import asyncio

async def main():
    prompt = "Check my age status"
    # name_input = input("Enter your Name: ")
    age_input = int(input("Enter your Age: "))

    context = AgeContext(age=age_input)

    agent = Agent(
        name="AgeChecker",
        instructions="An agent that checks if a person is an adult or a minor based on their age.",
        tools=[check_age],
    )

    result = await Runner(agent, prompt, run_config=config, context=context).run()
    print(result.output)

# Run the async main function
if __name__ == "__main__":
    asyncio.run(main())
