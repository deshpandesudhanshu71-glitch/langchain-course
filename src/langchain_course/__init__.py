from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()  # reads ANTHROPIC_API_KEY from .env


def main() -> None:
    llm = ChatAnthropic(model="claude-haiku-5-5")
    response = llm.invoke("Hello! Introduce yourself in one sentence.")
    print(response.content)


if __name__ == "__main__":
    main()
