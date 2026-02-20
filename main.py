import time
import requests


CITIES = [
    "Лондон",
    "Шереметьево",
    "Череповец"
]

URL_TEMPLATE = "http://wttr.in/{}?lang=ru&m&n&q&T"
HEADERS = {"User-Agent": "curl/8.0"}


def get_weather(city_name):
    url = URL_TEMPLATE.format(city_name)
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.text


def main():
    for city in CITIES:
        print(get_weather(city))
        time.sleep(1)


if __name__ == "__main__":
    main()