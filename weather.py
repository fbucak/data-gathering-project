import requests
import time


def location(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    location = data['location']['name']
    return location.title()

def date(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    date = data['forecast']['forecastday'][0]['date']
    return date.title()

def max_temp(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    max_temp = data['forecast']['forecastday'][0]['day']['maxtemp_c']
    return 'H: ' + str(round(max_temp)) + ' C'

def min_temp(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    min_temp = data['forecast']['forecastday'][0]['day']['mintemp_c']
    return 'L: ' + str(round(min_temp)) + ' C'

def condition(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    condition = data['forecast']['forecastday'][0]['day']['condition']['text']
    return condition.title()

def icon_url(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    icon_url = data['forecast']['forecastday'][0]['day']['condition']['icon']
    return 'https:' + icon_url

def date1(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    date1 = data['forecast']['forecastday'][1]['date']
    return date1.title()

def max_temp1(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    max_temp1 = data['forecast']['forecastday'][1]['day']['maxtemp_c']
    return 'H: ' + str(round(max_temp1)) + ' C'

def min_temp1(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    min_temp1 = data['forecast']['forecastday'][1]['day']['mintemp_c']
    return 'L: ' + str(round(min_temp1)) + ' C'

def condition1(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    condition1 = data['forecast']['forecastday'][1]['day']['condition']['text']
    return condition1.title()

def icon_url1(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    icon_url1 = data['forecast']['forecastday'][1]['day']['condition']['icon']
    return 'https:' + icon_url1

def date2(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    date2 = data['forecast']['forecastday'][2]['date']
    return date2.title()

def max_temp2(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    max_temp2 = data['forecast']['forecastday'][2]['day']['maxtemp_c']
    return 'H: ' + str(round(max_temp2)) + ' C'

def min_temp2(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    min_temp2 = data['forecast']['forecastday'][2]['day']['mintemp_c']
    return 'L: ' + str(round(min_temp2)) + ' C'

def condition2(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    condition2 = data['forecast']['forecastday'][2]['day']['condition']['text']
    return condition2.title()

def icon_url2(city):
    url = f'http://api.weatherapi.com/v1/forecast.json?key=e80b254046214aaf9e5154754220607&q={city}&days=3&aqi=no&alerts=no'
    req = requests.get(url) 
    data = req.json()
    icon_url2 = data['forecast']['forecastday'][2]['day']['condition']['icon']
    return 'https:' + icon_url2
    # date1 = data['forecast']['forecastday'][1]['date']
    # max_temp1 = data['forecast']['forecastday'][1]['day']['maxtemp_c']
    # min_temp1 = data['forecast']['forecastday'][1]['day']['mintemp_c']
    # condition1 = data['forecast']['forecastday'][1]['day']['condition']['text']
    # date2 = data['forecast']['forecastday'][2]['date']
    # max_temp2 = data['forecast']['forecastday'][2]['day']['maxtemp_c']
    # min_temp2 = data['forecast']['forecastday'][2]['day']['mintemp_c']
    # condition2 = data['forecast']['forecastday'][2]['day']['condition']['text']



