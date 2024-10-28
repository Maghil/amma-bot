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
        print(prompt)
        response = self.ai_client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        print(response.choices[0].message.content)
        return "a"


if __name__ == "__main__":
    prompt = "Provide a list of sentences in Tanglish, separated by semi-colons without numbering, as if from a concerned Tamil mom when a child says bye, sorted by clarity and fluency."
    ai_client = OpenAI(
            api_key=OPEN_AI_KEY
        )
    response=ai_client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    print((response.choices[0].message.content).split(";"))
