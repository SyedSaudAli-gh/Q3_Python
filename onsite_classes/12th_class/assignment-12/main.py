import geminiConfig
from agents import Agent, Runner, RunContextWrapper, function_tool, RunContextWrapper, input_guardrail,GuardrailFunctionOutput
from pydantic import BaseModel


class Account(BaseModel):
    name: str
    pin: int


class Guardrail_output(BaseModel):
    is_bank_related: bool

guardrail_agent = Agent(
    name="Guardrail Agent",
    instructions="check if the user is asking you bank related quries.",
    output_type = Guardrail_output,
)

@input_guardrail
async def check_bank_related(ctx:RunContextWrapper[None], agent:Agent, input:str) -> GuardrailFunctionOutput:

    result = await Runner.run(guardrail_agent, input, context=ctx.context, run_config = geminiConfig.config)

    guardrail_instance = GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_bank_related,
    )
    return guardrail_instance

def check_user(ctx:RunContextWrapper[Account], agent:Agent) -> bool:
    if ctx.context.name == "Saud" and ctx.context.pin == 1234:
        return True
    else:
        return False

@function_tool(is_enabled = check_user)
def check_balance(account_number: str) -> str:
    return f"The balance of the account is $1000000"

bank_agent = Agent(
    name = "Bank Agent",
    instructions = "You are a bank agent. You help customers with their questions you can use the tools to get the information you need.",
    tools = [check_balance],
    input_guardrails=[check_bank_related],

)

user_context = Account(name ="Saud", pin = 1234)

result = Runner.run_sync(bank_agent, "what is my balance my account no is 91234568", context = user_context, run_config = geminiConfig.config)


print(result.final_output)


