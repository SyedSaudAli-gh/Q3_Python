import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
import asyncio

# Load environment variables
load_dotenv()

# Get Gemini API Key
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set in the .env file")

# Gemini API setup
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

# Activity suggester agent
activity_suggester = Agent(
    name="Activity Suggester",
    instructions="""
    You are an activity suggestion agent.
    If the user's mood is "sad" or "stressed", suggest a helpful activity to improve their mood.
    Respond in this format:
    Suggested Activity: [Activity]
    Reason: [Why it helps]
    """,
    model=model
)

# Mood analyzer agent with automatic handoff
mood_analyzer = Agent(
    name="Mood Analyzer",
    instructions="""
    You are a mood detection agent.
    Read the user's message and classify their mood as one of the following:
    If mood is 'happy', 'angry', 'neutral', hand off to Activity Suggester agent.
    If mood is 'sad' or 'stressed', hand off to Activity Suggester agent.
    Otherwise just return the mood.
    Only return mood or let handoff agent reply.
    """,
    model=model,
    handoffs=[activity_suggester]
)

# Main logic
async def main():
    user_message = input("How are you feeling today? ")

    result = await Runner.run(
        mood_analyzer,
        input=user_message,
        run_config=config
    )

    # print("\nFinal Output:")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
