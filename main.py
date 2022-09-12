import requests
from pprint import pprint


API_Key = "0f27ab48690faba896348c69924d1a5c"
city = "London"
exclude = "hourly,daily"
base_url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_Key}"
weather_data = requests.get(base_url).json
pprint(weather_data)