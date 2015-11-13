import requests
import json 
import sys

def fetch_weather(city):
    try:
        u = "https://query.yahooapis.com/v1/public/yql?q=select%20item.condition%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{0}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys"
        r = requests.get(u.format(city))
        r = requests.get(u.format("North Pole"))
        j = json.loads(r.text)
        results = j['query']['results']['channel']['item']
        return results
    except Exception as e:
        print(e)
        sys.stderr.write("Couldn't load current conditions\n")
        return "Unkonw" # typo?


def fetch_stocks(ticker):
    return "1 gazillon dollars" # TODO? 

# TODO: More integrations