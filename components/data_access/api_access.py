import requests
from pprint import pprint



url2 = 'http://api.openweathermap.org/data/2.5/forecast?lat=35&lon=139&appid=620b3e5133182bab59eae994144f82a3&units=metric'

res = requests.get(url2)

data = res.json()
