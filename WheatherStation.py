from requests import get
import json
from pprint import pprint
from haversine import haversine 

#list of avaliable weather observatories
url = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
stations = get(url).json()['items']
pprint(stations)

#specefic observatory data
pprint('Liceo Scientifico Statale "Fermi-Monticelli')
urlId = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/17650487'
weatherData = get(urlId).json()['items']
pprint(weatherData)

