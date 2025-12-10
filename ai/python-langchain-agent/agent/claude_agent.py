from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from langchain.agents.structured_output import ToolStrategy

from agent.data import Context, ResponseFormat
from config import prompts
from agent import tools
import os


def _create_claude_sonnet_agent():
    # Add memory to maintain state across interactions and
    # allows the agent to remember previous conversations and context.
    checkpointer = InMemorySaver()

    # Get the model name
    model_name = os.getenv('CLAUDE_SONNET_NAME')

    # Create the model
    model = init_chat_model(
        model_name, #"claude-sonnet-4-5-20250929",
        temperature=0.5,
        timeout=10,
        max_tokens=1000
    )

    # Create agent
    agent = create_agent(
        model=model,
        system_prompt=prompts.SYSTEM_PROMPT,
        tools= tools.agent_tools_list,     # Set the tools in tools.py
        context_schema=Context, # Set the Context
        response_format=ToolStrategy(ResponseFormat),
        checkpointer=checkpointer
    )

    return agent


def _create_claude_opus_agent():
    # Add memory to maintain state across interactions and
    # allows the agent to remember previous conversations and context.
    checkpointer = InMemorySaver()

    # Get the model name
    model_name = os.getenv('CLAUDE_OPUS_NAME')

    # Create the model
    model = init_chat_model(
        model_name, #"claude-sonnet-4-5-20250929",
        temperature=0.5,
        timeout=10,
        max_tokens=1000
    )

    # Create agent
    agent = create_agent(
        model=model,
        system_prompt=prompts.SYSTEM_PROMPT,
        tools= tools.agent_tools_list,     # Set the tools in tools.py
        context_schema=Context, # Set the Context
        response_format=ToolStrategy(ResponseFormat),
        checkpointer=checkpointer
    )

    return agent




@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
        model_name = os.getenv('CLAUDE_SONNET_NAME')
    else:
        model_name = os.getenv('CLAUDE_OPUS_NAME')

    # Create the model
    model = init_chat_model(
        model_name,
        temperature=0.5,
        timeout=10,
        max_tokens=1000
    )
    return handler(request.override(model=model))


agent = create_agent(
    model=_create_claude_sonnet_agent,  # Default model
    tools=tools.agent_tools_list,
    middleware=[dynamic_model_selection])



