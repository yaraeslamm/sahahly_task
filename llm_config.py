from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY") 

llm = ChatGroq(
    temperature=0.3,
    model_name="llama-3.1-8b-instant",
    groq_api_key=GROQ_API_KEY
)