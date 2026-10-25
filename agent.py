from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain.tools import tool
import os
from langchain_groq import ChatGroq
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver


# tool
@tool
def google_search(query:str)->str:
    """
     Search Google for up to date information on the web.

     Args: query: What to search on google

     Returns: Top Search result as plain text 
    """

    search = GoogleSerperAPIWrapper(serper_api_key=os.getenv('SERPER_API_KEY'))

    return search.run(query)

# LLM - groq
llm = ChatGroq(model='openai/gpt-oss-120b', api_key=os.getenv('GROQ_API_KEY'))


# System prompt

SYSTEM_PROMPT = """
  You are a helpful research assistant with access of google
"""

# agent
agent = create_agent(
    model=llm,
    tools=[google_search],
    system_prompt=SYSTEM_PROMPT,
)

# result = agent.invoke({
#     "messages":[
#         {
#             "role":"user",
#             "content":"How's you?"
#         }
#     ]
# } , config={"configurable":{"thread_id":"1"}})

# print(result['messages'][-1].content)


