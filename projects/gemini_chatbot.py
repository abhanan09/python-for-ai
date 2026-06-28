import os
from google import genai
from google.genai import types

api_key = os.environ.get("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a friendly customer support assistant for 'Sweet Treats Bakery'. Only answer questions about the bakery's products, hours, and orders. Bakery hours are 9 AM to 7 PM, Monday to Saturday. You sell cakes, cupcakes, and pastries. If asked anything unrelated to the bakery, politely redirect the conversation back to bakery topics."
    ),
)

print("🤖 Sweet Treats Bakery Assistant (type 'quit' to exit)\n")

while True:
    user_input = input("You :")

    if user_input.lower() == "quit":
        print("Bot: Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print("Bot:", response.text)
    except Exception as e:
        print("Bot: Sorry, I'm having trouble responding right now. Please try again.")
