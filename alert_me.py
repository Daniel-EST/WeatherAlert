from open_weather_class import OpenWeatherClass
from telegram_class import TelegramClass
from notify_weather import notify_weather

# Getting Keys
with open('api_keys') as text_obj:
    open_weather_key = text_obj.readline().strip()
    telegram_key = text_obj.readline().strip() + '/'
    telegram_chat_id = text_obj.readline().strip()

city_ids = '3451190,6319198,3456282,3451189'    
open_weather = OpenWeatherClass(open_weather_key, 'metric', city_ids)

telegram = TelegramClass(telegram_key, telegram_chat_id)

time = (5,30,00)

print('\nI will alert you about the weather!')

try:
    notify_weather(open_weather, telegram, time)
except KeyboardInterrupt:
    print('Quitting the programm!')