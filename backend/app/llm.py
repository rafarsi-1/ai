import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# For xAI: Use requests instead
# import requests
# def generate_response_xai(prompt):
#     response = requests.post("https://api.x.ai/v1/chat/completions", json={
#         "model": "grok-4", "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}]
#     }, headers={"Authorization": f"Bearer {os.getenv('XAI_API_KEY')}"})
#     return response.json()['choices'][0]['message']['content']

def generate_response(character_desc: str, history: list, user_message: str):
    system_prompt = f"You are {character_desc}. Respond in character."
    messages = [{"role": "system", "content": system_prompt}] + history + [{"role": "user", "content": user_message}]
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)
    return response.choices[0].message.content