import requests
import time

cities = ["Лондон", "Шереметьево", "Череповец"]
url_template = "http://wttr.in/{}?lang=ru&m&n&q&T"

headers = {"User-Agent": "curl/8.0"}

for city in cities:
    url = url_template.format(city)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    print(response.text)
    time.sleep(1)  