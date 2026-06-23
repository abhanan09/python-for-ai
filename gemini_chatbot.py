import os
from google import genai

api_key = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

chat = client.chats.create(model="gemini-2.5-flash")


print("🤖 Gemini Chatbot (type 'quit' to exit)\n")

while True:
    user_input = input("You :")

    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    response = chat.send_message(user_input)
    print("Bot:", response.text)
