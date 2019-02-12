import json
import time
import datetime

import requests

# Open Weather API
weather_api_url = 'https://api.openweathermap.org/data/2.5/'

cities = {
    'nova_iguacu': '6319198',
    'rio_de_janeiro': ',3451190',
    'niteroi': ',3456282',
    'estado_rj': ',3451189'
    }
    
unity = '&units=metric'

query = 'group?id='
for key in cities.keys():
     query += cities[key]
     
with open('api_key_open_weather.txt') as k_obj:
    open_w_key = k_obj.read()
    api_key_open_weather = '&appid=' + open_w_key
    
req_url = weather_api_url + query + unity +  api_key_open_weather

# Telegram API
api_key_telegram = 'https://api.telegram.org/bot'

with open('api_key_telegram.txt') as k_obj:
    api_key_telegram += k_obj.read()

method = '/sendMessage?'

chat_id = 'chat_id=731152904&text='

text = 'Curently weather'

while True:
    if datetime.datetime.now() == 5:
        req = requests.get(req_url)

        if req.status_code==200:
            json_obj = req.json()
    
            for city in json_obj['list']:
                text = 'Curently weather in %s: %s' % (city['name'], city['weather'][0]['description'].title())
                requests.get(api_key_telegram + method + chat_id + text)
        
                if city['weather'][0]['icon'] in ['01d', '02d', '01n', '02n']:
                    text = 'I think you don\'t need an umbrella today.'
                    requests.get(api_key_telegram + method + chat_id + text)
                
                else:
                    text = 'I would consider having a umbrella a good ideia today'
                    requests.get(api_key_telegram + method + chat_id + text)        
            
                text = 'Max tempture: %i' % city['main']['temp_max']
                requests.get(api_key_telegram + method + chat_id + text)
                text = 'Min tempture: %i' % city['main']['temp_min']
                requests.get(api_key_telegram + method + chat_id + text)
        
                if  city['main']['temp_max'] < 25 or city['main']['temp_min'] < 25:
                    text = 'Don\'t forget your coat!'
                    requests.get(api_key_telegram + method + chat_id + text)
            
                print('\n\n')
            
        time.sleep(60 * 60)