from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse
from dotenv import load_dotenv

from agent import tools
import os

# Load the environment variables
load_dotenv()

# Create the OpenAI models
_openai_basic_model = ChatOpenAI(model=os.getenv('OPENAI_MINI_NAME'))
_openai_advanced_model = ChatOpenAI(model=os.getenv('OPENAI_MODEL_NAME'))


@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
        model = _openai_advanced_model
    else:
        model = _openai_basic_model

    return handler(request.override(model=model))


agent = create_agent(
    model=_openai_basic_model,  # Default model
    tools=tools.agent_tools_list,
    middleware=[dynamic_model_selection])