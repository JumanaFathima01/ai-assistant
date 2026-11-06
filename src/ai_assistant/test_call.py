import os
from dotenv import load_dotenv
from openai import OpenAI
from ai_assistant.load import load_text

load_dotenv()

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    timeout=120,
    max_retries=0,
)

try:
    response = client.chat.completions.create(
        model="gemini-flash-latest",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Say hi in one sentence."},
        ],
    )
    print(response.choices[0].message.content)
except Exception as e:
    print("ERROR TYPE:", type(e).__name__)
    print("MESSAGE:", e)
    print("BODY:", getattr(e, "body", None))
    print("URL:", getattr(getattr(e, "request", None), "url", None))


print(load_text("resume.txt"))
