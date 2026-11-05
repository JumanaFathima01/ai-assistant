import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class ResumeScreener:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ["GEMINI_API_KEY"],
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            timeout=120,
            max_retries=0,
        )

    def screen(self, resume, job):
        response = self.client.chat.completions.create(
            model="gemini-3.1-flash-lite",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Screen the following resume for the job description: {job}. Resume: {resume}",
                },
            ],
        )
        return response.choices[0].message.content
