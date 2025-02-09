import os
import time
import requests
from dotenv import load_dotenv

import google.generativeai as genai 

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

class Waha:

    def __init__(self):
        self.__api_url = 'http://waha:3000'

    def generate_custom_message(self, message: str) -> str:
        model = genai.GenerativeModel("gemini-1.5-flash") 
    
        response = model.generate_content( 
            message, 
            generation_config = genai.GenerationConfig(max_output_tokens=300,) 
        ) 

        return str(response.text)

    def send_message(self, chat_id, message):
        url = f'{self.__api_url}/api/sendText'
        headers = {
            'Content-Type': 'application/json'
        }

        get_custom_message = self.generate_custom_message(message)

        time.sleep(4)

        payload = {
            'session': 'default',
            'chatId': chat_id,
            'text': get_custom_message
        }

        print('payload', payload)

        try:
            response = requests.post(url, json=payload, headers=headers)

            response.raise_for_status()

            return response.json()
        
        except requests.exceptions.RequestException as e:
            print(f"Erro ao enviar mensagem: {e}")
            return None