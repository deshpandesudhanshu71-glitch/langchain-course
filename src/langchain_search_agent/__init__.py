import os

from dotenv import load_dotenv
load_dotenv()
from langchain.agents import create_agent
from langchain.tools import tool 
from langchain_anthropic import ChatAnthropic 
from tavily import TavilyClient
from langchain_core.messages import HumanMessage
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def search_web(query: str) -> str:
    """Search the web for information about the query""" 

    """ 
    Tool that search over the internet 
    Args:
        query: The query to search for 
    Returns:
        The search results 
    """
    
    print(f"Searching the web for {query}")
    return tavily.search(query = query)

llm = ChatAnthropic(model="claude-sonnet-5-5", anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")) 
tools = [search_web]
agent = create_agent(model = llm, tools = tools)

def main() -> None:
    print("Hello from langchain-search-agent!")
    result = agent.invoke({"messages": [HumanMessage(content="search for 3 jobs posting for ai engineer using langchain in ireland on linkdin and list their details")]})
    print(result)

if __name__ == "__main__":
    main()
