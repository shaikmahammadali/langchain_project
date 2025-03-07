# langchain_project

# Project Overview
This project implements a LangChain application that integrates multiple chat models including OpenAI's GPT, Google's Gemini, and Anthropic's models.

# Installation
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```

# Environment Variables
Create a `.env` file in the root directory of the project with the following content:
```
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
```
Make sure to replace the placeholders with your actual API keys and the path to your service account credentials.

# Usage
To use the chat models, you can invoke them as follows:
```python
result = model.invoke("Hello, how are you?")
print(result.content)
```

# Models
- **OpenAI**: Uses the `ChatOpenAI` model from `langchain_openai`.
- **Google Gemini**: Uses the `ChatGoogleGenerativeAI` model for interaction with Google's Gemini API.
- **Anthropic**: Implementation details to be added.