import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

print(os.environ["GEMINI_API_KEY"][:5])
