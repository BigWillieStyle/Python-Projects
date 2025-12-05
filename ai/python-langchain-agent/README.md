Python LangChain Agent Project
- Simple AI agent project using LangChain

1) Use UV to create project. Below is the link to install UV Python package Manager
   Link: https://docs.astral.sh/uv/guides/install-python/

2) Create project folder -> mkdir python-langchain-agent

3) In the project folder at command Line ->  uv init .

4) Install dependencies -> uv add langchain langgraph python-dotenv langchain-openai

Running the project
1) Create .env file in the project folder.  In the file add the OpenAI API Key.  Below is the link to obtain an API key.
   Link: https://platform.openai.com/api-keys

2) In the .env file add the following entry along with the Claude.ai API Key
   ANTHROPIC_API_KEY=<API KEY>

3) Run project using UV
   uv run main.py
 
Note:
This project is designed to explore the LangChain functionality such as:
    - Key production concepts - https://docs.langchain.com/oss/python/langchain/quickstart
      - Detailed system prompts for better agent behavior
      - Create tools that integrate with external data
      - Model configuration for consistent responses
      - Structured output for predictable results
      - Conversational memory for chat-like interactions
      - Create and run the agent create a fully functional agent
    - Agents (Static vs Dynamic) - https://docs.langchain.com/oss/python/langchain/agents
    - Models - https://docs.langchain.com/oss/python/langchain/models
    - Messages - https://docs.langchain.com/oss/python/langchain/messages
    - Tools (@tools) - https://docs.langchain.com/oss/python/langchain/tools
    - Short-term memory - https://docs.langchain.com/oss/python/langchain/short-term-memory
    - Streaming - https://docs.langchain.com/oss/python/langchain/streaming
    - Structured Output - https://docs.langchain.com/oss/python/langchain/structured-output
    - Custom Middleware (@wrap_model_call) - https://docs.langchain.com/oss/python/langchain/middleware/custom