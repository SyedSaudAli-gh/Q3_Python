import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, ModelSettings, function_tool
from agents.run import RunConfig
import asyncio
from typing import List, Optional
from dataclasses import dataclass
# from agents import set_default_openai_key

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

@dataclass
class Purchase:
    id: str
    name: str
    price: float
    date: str
    
@dataclass
class UserContext:
    uid: str
    is_pro_user: bool
    
    async def fetch_purchases(self) -> List[Purchase]:
        # This is a mock implementation
        # In a real application, this would fetch from a database
        if self.uid == "user123":
            return [
                Purchase(id="p1", name="Basic Plan", price=9.99, date="2023-01-15"),
                Purchase(id="p2", name="Premium Add-on", price=4.99, date="2023-02-20")
            ]
        return []

@function_tool
async def get_user_info(context: UserContext) -> str:
    """Get basic information about the current user"""
    user_type = "Pro" if context.is_pro_user else "Free"
    return f"User ID: {context.uid}, Account Type: {user_type}"

@function_tool
async def get_purchase_history(context: UserContext) -> str:
    """Get the purchase history for the current user"""
    purchases = await context.fetch_purchases()
    if not purchases:
        return "No purchase history found."
    
    result = "Purchase History:\n"
    for p in purchases:
        result += f"- {p.name}: ${p.price} on {p.date}\n"
    return result

@function_tool
async def get_personalized_greeting(context: UserContext) -> str:
    """Get a personalized greeting based on user status"""
    if context.is_pro_user:
        return "Welcome back to our premium service! We value your continued support."
    else:
        return "Welcome! Consider upgrading to our Pro plan for additional features."
    


user_context_agent = Agent[UserContext](
    name="User Context Agent",
    instructions="""
    You are a helpful assistant that provides personalized responses based on user context.
    Use the available tools to retrieve user information and provide tailored assistance.
    For pro users, offer more detailed information and premium suggestions.
    """,
    tools=[get_user_info, get_purchase_history, get_personalized_greeting],
)

async def main():    
    # Create sample users
    pro_user_context = UserContext(uid="user123", is_pro_user=True)
    free_user_context = UserContext(uid="user456", is_pro_user=False)
    
    # Example with pro user
    print("\n--- Pro User Example ---")
    result = await Runner.run(
        user_context_agent, 
        "Tell me about myself and my purchases", 
        context=pro_user_context,
        run_config=config
    )
    print("Response for Pro User:", result.final_output)
    
    # Example with free user
    print("\n--- Free User Example ---")
    result = await Runner.run(
        user_context_agent, 
        "Tell me about myself and my purchases", 
        context=free_user_context,
        run_config=config
    )
    print("Response for Free User:", result.final_output)

if __name__ == "__main__":
    asyncio.run(main()) 