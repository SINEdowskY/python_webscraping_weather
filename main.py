from urllib.request import urlopen
from bs4 import BeautifulSoup
import unicodedata


def strip_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')


def weather(place):
    city = strip_accents(str(place))
    html = urlopen('https://www.meteoprog.pl/pl/weather/{}/'.format(city))
    bs = BeautifulSoup(html, 'html.parser')

    weather = bs.find('section', class_='today-block')

    title = str(weather.h1.contents[0]).replace("Pogoda ", "")
    date_time = weather.h2.contents[0]
    current_temperature = str(weather.find('div', class_='today-temperature').contents[0]).strip()
    description = weather.h3.contents[0]

    print(title)
    print(date_time)
    print(current_temperature)
    print(description)

   # to_json = """
    #{
    #    "city": {},
    #    "date_time_place": {},
    #    "current_temperature": {},
    #    "description": {}
    
   #}
    
    #""".format(title, date_time, current_temperature, description)


weather('Rzeszów')


