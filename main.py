from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"

)

def chatWithGPT(prompt):
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    while True:
        userInput = input("You: ")
        if userInput.lower() in ["quit", "exit", "bye"]:
            break

        response = chatWithGPT(userInput)
        print("Chatbot: ", response)