from openai import OpenAI
from dotenv import load_dotenv
import os
from document_handler import extract_text

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"

)
SYSTEM_PROMPT = """You are a helpful and friendly assistant that helps students understand their course syllabus.
Only answer questions based on the syllabus content provided below.
If the answer isn't in the syllabus, say so clearly instead of guessing.
Keep your tone approachable, realistic,  and concise, like a knowledgeable classmate."""

def chatWithGPT(syllabus_text, user_question):
    response = client.chat.completions.create(
        model="openai/gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Syllabus content: \n{syllabus_text}\n\n Question: {user_question}\n"}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    syllabus_path = "Course_Syllabus.pdf"
    syllabus_text = extract_text(syllabus_path)

    if not syllabus_text:
        print("Failed to extract text from syllabus. Please try again.\n")

    print("Syllabus loaded! Ask me anything about it.\n")
    while True:
        userInput = input("You: ")
        if userInput.lower() in ["quit", "exit", "bye"]:
            break

        response = chatWithGPT(syllabus_text, userInput)
        print("Chatbot: ", response)