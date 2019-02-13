import requests

class TelegramClass():
    def __init__(self, key, chat_id):
        self.key = key
        self.chat_id = chat_id
        
    def send_message(self, text):
        request = 'https://api.telegram.org/bot'
        request += self.key
        request += 'sendMessage?'
        
        request_params = {
            'chat_id': self.chat_id,
            'text': text,
            }
        requests.get(request, params=request_params)