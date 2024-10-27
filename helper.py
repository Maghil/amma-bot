from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')

class AiHelper:
    def __init__(self) -> None:
        self.ai_client = OpenAI(
            api_key=OPEN_AI_KEY
        )

    def getResponse(self, prompt):
        response = self.ai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
