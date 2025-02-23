import os
from langchain_google_genai import ChatGoogleGenerativeAI  # Correct import
from dotenv import load_dotenv
# Load API Key from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")  # Correct variable name
# Ensure the API key is loaded correctly
if not gemini_api_key:
    raise ValueError("API key not found. Please check your .env file.")
# Initialize LangChain with Google Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-pro", api_key=gemini_api_key)
# Run a simple query
# response = llm.invoke("What is LangChain?")
test_query = "Explain LangChain in detail as an AI framework."
response = llm.invoke(test_query)
# Correct way to print response
print(response.content)  # Extracts the actual text response
# # If You Are Using OpenAI Instead of Google, Use This Import
# import os
# from langchain_openai import OpenAI
# from dotenv import load_dotenv
# # Load API Key
# load_dotenv()
# openai_api_key = os.getenv("OPENAI_API_KEY")
# # Initialize LangChain with OpenAI LLM
# llm = OpenAI(api_key=openai_api_key)
# # Run a simple query
# response = llm.invoke("What is LangChain?")
# print(response)
