import os
import requests
from dotenv import load_dotenv

import google.generativeai as genai 

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

class Waha:

    def __init__(self):
        self.__api_url = 'http://waha:3000'

    def send_message(self, chat_id, message):
        url = f'{self.__api_url}/api/sendText'
        headers = {
            'Content-Type': 'application/json'
        }

        payload = {
            'session': 'default',
            'chatId': chat_id,
            'text': message
        }

        try:
            response = requests.post(url, json=payload, headers=headers)

            response.raise_for_status()

            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")
            return None
    
    def start_typing(self, chat_id):
        url = f'{self.__api_url}/api/startTyping'
        
        headers = {
            'Content-Type': 'application/json'
        }

        payload = {
            'session': 'default',
            'chatId': chat_id
        }

        requests.post(
            url=url,
            json=payload,
            headers=headers
        )

    def stop_typing(self, chat_id):
        url = f'{self.__api_url}/api/stopTyping'
        
        headers = {
            'Content-Type': 'application/json'
        }

        payload = {
            'session': 'default',
            'chatId': chat_id
        }

        requests.post(
            url=url,
            json=payload,
            headers=headers
        )

    def generate_custom_message(self, message: str) -> str:
        model = genai.GenerativeModel("gemini-1.5-flash") 
    
        response = model.generate_content( 
            message, 
            generation_config = genai.GenerationConfig(max_output_tokens=300,) 
        ) 

        return str(response.text)