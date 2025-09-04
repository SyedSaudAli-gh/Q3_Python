import geminiConfig
from agents import Agent, Runner, function_tool


@function_tool
def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

support_agent = Agent(
    name="Support Agent",
    instructions="You are a support agent. Answer questions about the Gemini API and its usage.",
    tools=[greet],
)

prompt = input("Enter your question: ")

result = Runner.run_sync(support_agent, prompt, run_config=geminiConfig.config )

print(result.final_output)