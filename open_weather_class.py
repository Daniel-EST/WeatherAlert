import requests

class OpenWeatherClass():
    def __init__(self, appid, units, id):
        self.appid = appid
        self.units = units
        self.id = id
        
    def get_weather(self):
    
        request = 'https://api.openweathermap.org/data/2.5/'
        request += 'group?'

        request_params = {
            'appid': self.appid,
            'units': self.units,
            'id': self.id,
            }
        return requests.get(request, params=request_params)