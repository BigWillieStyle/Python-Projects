#
# Structured output allows agents to return data in a specific, predictable format.
# Instead of parsing natural language responses, you get structured data in the form
# of JSON objects, Pydantic models, or dataclasses that your application can directly use.
#
# LangChain’s create_agent handles structured output automatically. The user sets their
# desired structured output schema, and when the model generates the structured data,
# it’s captured, validated, and returned in the 'structured_response' key of the agent’s state.
#

from dataclasses import dataclass

# Declare context schema data class for agents
@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str

# We use a dataclass here, but Pydantic models are also supported.
# Controls how the agent returns structured data:
@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A punny response (always required)
    punny_response: str
    # Any interesting information about the weather if available
    weather_conditions: str | None = None