from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import wrap_model_call, ModelRequest, ModelResponse

from tools import agent_tools_list

openai_basic_model = ChatOpenAI(model="gpt-4o-mini")
openai_advanced_model = ChatOpenAI(model="gpt-4o")

@wrap_model_call
def dynamic_model_selection(request: ModelRequest, handler) -> ModelResponse:
    """Choose model based on conversation complexity."""
    message_count = len(request.state["messages"])

    if message_count > 10:
        # Use an advanced model for longer conversations
        model = openai_advanced_model
    else:
        model = openai_basic_model

    return handler(request.override(model=model))

agent = create_agent(
    model=openai_basic_model,  # Default model
    tools=agent_tools_list,
    middleware=[dynamic_model_selection])