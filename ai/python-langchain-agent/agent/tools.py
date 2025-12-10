# Tools are components that agents call to perform actions. They extend model
# capabilities by letting them interact with the world through well-defined inputs and outputs.
#
# Tools encapsulate a callable function and its input schema. These can be passed
# to compatible chat models, allowing the model to decide whether to invoke a tool
# and with what arguments. In these scenarios, tool calling enables models to generate
# requests that conform to a specified input schema.
#
# Basic tool definition
# The simplest way to create a tool is with the @tool decorator. By default,
# the function’s docstring becomes the tool’s description that helps the model
# understand when to use it
#
# Link: https://docs.langchain.com/oss/python/langchain/tools

from langchain.tools import tool, ToolRuntime

from agent.data import Context # import context schema class

# Declare get weather for location tool
@tool
def get_weather_for_location(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


# Declare get user location tool
@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "SF"


agent_tools_list = [get_user_location, get_weather_for_location]