from datetime import datetime
from html.parser import HTMLParser
import json
import requests

def getDatafromAPI(value, currency, timespan, interval):
    text = requests.get(f"https://api.coingecko.com/api/v3/coins/{value}/market_chart?vs_currency={currency}&days={timespan}&interval={interval}")
    #temp = text.text
    #temp = temp["prices"]
    #print(text.text)
    return text.text

def unJSON(file):
    stringDict = json.loads(file)
    #print(stringDict["prices"])
    stringDict = stringDict["prices"]
    return stringDict

def convertmsToTime(miliseconds):
    parsedms = int(miliseconds)
    #print(parsedms)
    dt = datetime.fromtimestamp(parsedms / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
    #print(dt)
    return dt

def translatingTohumanTime(data):
    for i in range(len(data)):
        data[i][0] = convertmsToTime(data[i][0])
    print(data)
    return data

file = getDatafromAPI("bitcoin", "usd", "1", "hourly")
#print()
data = unJSON(file)
print(data)
#convertmsToTime("1778342439151")
#convertmsToTime("1778346011378")
translatingTohumanTime(data)