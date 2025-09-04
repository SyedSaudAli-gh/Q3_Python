import geminiConfig
import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner

agent = Agent(
    name="Assistant Agent",
    instructions="You are a helpful assistant."
    )

async def main():
    
    prompt = input("Enter your prompt: ")

    result = Runner.run_streamed(agent, prompt, run_config=geminiConfig.config)
    async for e in result.stream_events():
        if e.type == "raw_response_event" and hasattr(e.data, "delta"):
            print(e.data.delta, end="", flush=True)

   
if __name__ == "__main__":
    asyncio.run(main())
            
