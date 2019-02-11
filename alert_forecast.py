import json
import time
import datetime

import requests

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
     
with open('api_key.txt') as k_obj:
    open_w_key = k_obj.read()
    api_key = '&appid=' + open_w_key
    
req_url = weather_api_url + query + unity + api_key

while True:
    if datetime.datetime.now() == 5
        req = requests.get(req_url)

        if req.status_code==200:
            json_obj = req.json()
    
            for city in json_obj['list']:
                print('Curently weather in %s: %s' % (city['name'], city['weather'][0]['description'].title()))
        
                if city['weather'][0]['icon'] in ['01d', '02d', '01n', '02n']:
                    print('I think you don\'t need an umbrella today.')
            
                else:
                    print('I would consider having a umbrella a good ideia today')        
            
                print('Max tempture: %i' % city['main']['temp_max'])
                print('Min tempture: %i' % city['main']['temp_min'])
        
                if  city['main']['temp_max'] < 25 or city['main']['temp_min'] < 25:
                    print('Don\'t forget your coat!')
            
                print('\n\n')
            
        time.sleep(60 * 60)
