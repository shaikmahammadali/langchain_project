from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(
    model="claude-3-5-sonnet",
    temperature=0.7,
    anthropic_api_key=os.getenv("ANTHROPIC_API_KEY")
)
result=model.invoke("Hello, how are you?")
print(result)
