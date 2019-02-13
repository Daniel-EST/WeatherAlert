import json
import time
import datetime

import requests

from open_weather_class import OpenWeatherClass
from telegram_class import TelegramClass

def notify_weather(weather, telegram, time):
    
    bad_weather = ['03d', '03n', '04d', '04n', '09d', '09n', '10d', '10n', '11d', '11n']
    
    while True:
        # Initializing Variables
        city_icons = []
        city_maxs = []
        city_mins = []
        text = ''
        dt_now = datetime.datetime.now()

        if (dt_now.hour, dt_now.minute, dt_now.second)==time:
            req = weather.get_weather()

            if req.status_code==200:
                json_obj = req.json()

                for city in json_obj['list']:
                    city_icons.append(city['weather'][0]['icon'])
                    city_maxs.append(city['main']['temp_max'])
                    city_mins.append(city['main']['temp_min'])
                
                    text += 'Curently weather in %s: %s\n' % (city['name'], city['weather'][0]['description'].title())
                    text += 'Max tempture: %i\n' % city['main']['temp_max']
                    text += 'Min tempture: %i\n\n' % city['main']['temp_min']
                
                for city_icon in city_icons:
                    if city_icon in bad_weather:
                        text += 'Please! Don\'t forget your umbrella! \u2614 \n'
                        break
                
                for city_max in city_maxs:
                    if city_max < 25 or city_mins.pop() < 25:
                        text += 'A coat would be a good idea!'
                        break
                    
                telegram.send_message(text)
            else:
                text = 'Sorry, I couldn\'t bring weather information for you today'
                telegram.send_message(text)