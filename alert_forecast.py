import json
import time
import datetime

import requests

from open_weather_class import OpenWeatherClass
from telegram_class import TelegramClass

# Getting Keys
with open('api_keys') as text_obj:
    open_weather_key = text_obj.readline().strip()
    telegram_key = text_obj.readline().strip() + '/'
    telegram_chat_id = text_obj.readline().strip()

city_ids = '3451190,6319198,3456282,3451189'    
open_weather = OpenWeatherClass(open_weather_key, 'metric', city_ids)

telegram = TelegramClass(telegram_key, telegram_chat_id)
    
while True:
    dt_now = datetime.datetime.now()
    if (dt_now.hour, dt_now.minute, dt_now.second)==(12,44,00):
        req = open_weather.get_weather()

        if req.status_code==200:
            json_obj = req.json()
    
            for city in json_obj['list']:
                text = 'Curently weather in %s: %s' % (city['name'], city['weather'][0]['description'].title())
        
                if city['weather'][0]['icon'] in ['01d', '02d', '01n', '02n']:
                    text += '\nI think you don\'t need an umbrella today.'
                
                else:
                    text += '\nI would consider having a umbrella a good ideia today'     
            
                text += '\nMax tempture: %i' % city['main']['temp_max']
                text += '\nMin tempture: %i' % city['main']['temp_min']
        
                if  city['main']['temp_max'] < 25 or city['main']['temp_min'] < 25:
                    text += '\nDon\'t forget your coat!'
                
                telegram.send_message(text)
        else:
            text = 'Sorry, I couldn\'t bring weather information for you today'
            telegram.send_message(text)