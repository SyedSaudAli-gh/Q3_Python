import geminiConfig
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner


async def main():
    agent = Agent(
        name="Gemini Agent",
        instructions="You are a helpful assistant."
        )
    
    prompt = input("Enter your prompt: ")

    result = Runner.run_streamed(agent, prompt, run_config=geminiConfig.config)

    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
            
