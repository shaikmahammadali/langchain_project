from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

# Load the Hugging Face chat model
hf_pipeline = pipeline("question-answering", model="nvidia/DeepSeek-R1-FP4")

# Create a LangChain HuggingFacePipeline instance
# it will download the model to our local
langchain_model = HuggingFacePipeline(pipeline=hf_pipeline) 

# Function to interact with the LangChain model
def chat_with_model(user_input):
    response = langchain_model(user_input)
    return response

# Example usage
if __name__ == "__main__":
    user_input = "Hello, how are you?"
    response = chat_with_model(user_input)
    print(response)