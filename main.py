import os
from dotenv import load_dotenv
load_dotenv()

def main():
    print("Hello from langchain-course!")
    api_key = os.getenv("OPENAI_API_KEY")
    print(f"OpenAI API key is set. {api_key}")


if __name__ == "__main__":
    main()
