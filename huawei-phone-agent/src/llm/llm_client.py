from openai import OpenAI
from dotenv import load_dotenv
import os


class HelloAgentsLLM:
    def __init__(self):
        load_dotenv()
        self.client = OpenAI(
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url=os.getenv("API_BASE").strip()
        )
        self.model = os.getenv("MODEL_NAME", "qwen-flash")

    def chat(self, messages):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return response.choices[0].message.content
