import asyncio

from pydantic_ai import Agent
from pydantic_ai.messages import ModelMessage
from pydantic_ai.models.openai import OpenAIResponsesModel
from pydantic_ai.providers.openai import OpenAIProvider
from rich.console import Console
from rich.markdown import Markdown

from coding_assistant.deps import AgentDeps
from coding_assistant.utils import get_env


async def run_agent() -> None:
    console = Console()

    console.print("Coding assistant ready. Type your request:")

    # 1. Configure the provider
    provider = OpenAIProvider(
        base_url=get_env("BASE_URL"),
        api_key=get_env("API_KEY"),
    )

    # 2. Configure the model
    model = OpenAIResponsesModel(
        model_name=get_env("MODEL_NAME"),
        provider=provider,
    )

    # 3. Create the agent. Attach the model and instructions
    agent = Agent(
        model=model,
        instructions=(
            "You are a Python coding assistant. "
            "Write clear, correct, and minimal Python code that runs as-is. "
            "Prefer the standard library and follow PEP 8 with type hints. "
            "By default, reply with code and no explanation. "
            "Explain your reasoning only when the user explicitly asks. "
            "If the request is ambiguous, ask one short clarifying question before coding. "
            "If you are unsure or cannot do something, say so instead of inventing APIs."
        ),
    )

    # 4. Conversation loop with message history
    message_history: list[ModelMessage] = []

    while True:
        user_input = console.input(">> ")
        result = await agent.run(user_input, message_history=message_history)
        console.print(Markdown(result.output))
        message_history = result.all_messages()


def main() -> None:
    try:
        asyncio.run(run_agent())
    except (EOFError, KeyboardInterrupt):
        pass
        
if __name__ == "__main__":
    main()
