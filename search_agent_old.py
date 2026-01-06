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
from langchain_classic.agents import AgentExecutor
from langchain_classic import hub
from langchain_classic.agents.react.agent import create_react_agent
from response_schema import AgentResponse
from prompt import react_prompt

load_dotenv()


# Create an instance of ChatOpenAI
llm = ChatOpenAI(model="gpt-4")
react_prompt = hub.pull("hwchase17/react") # connection issue
tools = [TavilySearch()]

# Create an agent using the search tool
# agent = create_agent(llm, tools, response_format=AgentResponse)

agent = create_react_agent(llm, tools, prompt=react_prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
chain = agent_executor

# Define a function to run the agent with a query
# def run_agent(query: str) -> str:
#     response = agent.run([HumanMessage(content=query)])
#     return response.content


def main():
    print("Hello from react-search-agent!")
    query = "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details"
    result = chain.invoke(input={"input": query})
    print(result)


if __name__ == "__main__":
    main()
