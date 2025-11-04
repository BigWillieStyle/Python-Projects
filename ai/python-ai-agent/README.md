Python AI Agent Project
- Simple AI aegnt project using LangChain

1) Use UV to creat project. Below is the link to install UV Python package Manager
   Link: https://docs.astral.sh/uv/guides/install-python/

2) Create project folder -> mkdir python-ai-agent

3) In the project folderr at command Line ->  uv init .

4) Install dependencies -> uv add langchain langgraph python-dotenv langchain-openai

Running the project
1) Create .env file in the project folder.  In the file add yourr OpenAI API Key.  Below is the link to obtain an API key.
   Link: https://platform.openai.com/api-keys

2) In the .env file add the following entry along with the API Key
   OPENAI_API_KEY=<API KEY>

3) Run project using UV 
   uv run main.py
 
