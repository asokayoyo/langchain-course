"""
The testing ground for react-search-agent project. That will create an agent that can use to search the web.
"""


# import langchain tools and human messages, langchain openai
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_tavily import TavilySearch
from tavily import TavilyClient
from pydantic import BaseModel, Field
from typing import List

load_dotenv()

class Source(BaseModel):
    """Schema for a source used by the agent."""
    url: str = Field(..., description="The URL of the source")
    
class AgentResponse(BaseModel):    
    """Schema for search results returned by the agent with answer and sources."""
    answer: str = Field(..., description="The agent's answer to the query")
    sources: List[Source] = Field(..., default_factory=list, description="List of sources used to generate the answer")

tavily = TavilyClient()

@tool
def search(query: str) -> str:
    """
    Deprecated: 
        this is custom tool to do the simple search using tavily. Now we can use TavilySearch from langchain_tavily
    Search the web for a query and return the results.
    Args:
        query (str): The search query.
    Returns:
        str: The search results.
    """
    # For demonstration purposes, we will return a mock result.
    # In a real implementation, you would integrate with a search API here.
    print(f"Searching the web for query: {query}")
    return tavily.search(query)


# Create an instance of ChatOpenAI
llm = ChatOpenAI(model="gpt-5-nano")

tools = [TavilySearch(tool=search, max_results=3, topic="general")]

# Create an agent using the search tool
agent = create_agent(llm, tools, response_format=AgentResponse)

# Define a function to run the agent with a query
# def run_agent(query: str) -> str:
#     response = agent.run([HumanMessage(content=query)])
#     return response.content


def main():
    print("Hello from react-search-agent!")
    query = "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
    result = agent.invoke({"messages": [HumanMessage(content=query)]})
    print(result)


if __name__ == "__main__":
    main()
