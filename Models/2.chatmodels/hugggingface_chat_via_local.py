from langchain_huggingface import HuggingFacePipeline,ChatHuggingFace
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv() 

# Load the Hugging Face chat model in  to local
llm = HuggingFacePipeline.from_model_id(model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                                                task="text-generation",
                                                pipeline_kwargs=dict(temperature=0.7,
                                                                    max_new_tokens=100)
                                                )
model=ChatHuggingFace(llm=llm)
result=model.invoke("what is the capital city of india ?")
print(result.content)




# Example usage
if __name__ == "__main__":
    user_input = "Hello, how are you?"
    response = chat_with_model(user_input)
    print(response)