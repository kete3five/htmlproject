from html.parser import HTMLParser
import json
import requests

def getDatafromAPI(value, currency, timespan, interval):
    text = requests.get(f"https://api.coingecko.com/api/v3/coins/{value}/market_chart?vs_currency={currency}&days={timespan}&interval={interval}")
    print(text.text)
    return text.text

def unJSON(file):
    stringDict = json.loads(file)
    print(stringDict["prices"])


file = getDatafromAPI("bitcoin", "usd", "15", "daily")
print()
unJSON(file)