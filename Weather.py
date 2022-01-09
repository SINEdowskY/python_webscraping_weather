from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata


class Weather:

    __weather_document = None
    city = None
    current_temerature = None

    def __init__(self, place):
        city = ''.join(c for c in unicodedata.normalize('NFD', place) if unicodedata.category(c) != 'Mn').replace(" ", "")
        html = urlopen('https://www.meteoprog.pl/pl/weather/{}/'.format(city))
        bs = BeautifulSoup(html, 'html.parser')
        self.weather_document = bs.find('section', class_='today-block')

    def get_weather(self):
        title = str(self.weather_document.h1.contents[0]).replace("Pogoda ", "").replace("na dziś", "")
        date_time = self.weather_document.h2.contents[0]
        current_temperature = str(self.weather_document.find('div', class_='today-temperature').contents[0]).strip()
        description = self.weather_document.h3.contents[0]

        print(title)
        print(date_time)
        print(current_temperature)
        print(description)
