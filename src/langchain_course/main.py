from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
import os
load_dotenv()  # reads ANTHROPIC_API_KEY from .env


def main() -> None:
    llm = ChatAnthropic(model="claude-haiku-5-5")
    response = llm.invoke("Hello! Introduce yourself in one sentence.")
    print(response.content)
    print("Hello wfrom langchain course")  
    print(os.environ.get("ANTHROPIC_API_KEY")) 

if __name__ == "__main__":
    main()