from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, RunContextWrapper, input_guardrail
from agents.run import RunConfig
from pydantic import BaseModel

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key = gemini_api_key,
    base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model = "gemini-2.0-flash",
    openai_client = client,
)

config = RunConfig(
    model=model,
    model_provider=client,
    tracing_disabled=True,
)

class Account(BaseModel):
    name: str
    pin: int

class Guardrail_Output(BaseModel):
    is_not_bank_related: bool

guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="check if the user is asking you bank related questions",
    output_type=Guardrail_Output
)

@input_guardrail
async def check_bank_related(ctx:RunContextWrapper[None], agent:Agent, input:str) -> Guardrail_Output:
    
    result = await Runner.run(guardrail_agent, input, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_not_bank_related
    )

def check_user(ctx: RunContextWrapper[Account], agent:Agent)-> bool:
    if ctx.context.name == "Saud" and ctx.context.pin == 1234:
        return True
    else:
        return False
    
@function_tool(is_enabled=check_user)
def check_balance(account_number:str) -> str:
    return f"Your balance for account {account_number} is $1000000."

bank_agent = Agent(
    name="Bank Agent",
    instructions="You are a bank agent. You help customers with their qestions you can use the tools to get the information",
    tools=[check_balance],
    input_guardrail=[check_bank_related   ],

)

user_context = Account(name="Saud", pin=  )

