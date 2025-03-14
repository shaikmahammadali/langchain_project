from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()
# with key specifying
# llm=HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
#                         task="text-generation",
#                         huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
#                         )
llm=HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                        task="text-generation"
                        )


model=ChatHuggingFace(llm=llm)
result=model.invoke("what is the capital city of india ?")
print(result.content)
