from flask import *
import random
from html.parser import HTMLParser

readyData = []

class overriddenHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
    def handle_data(self, data):
        global readyData
        readyData.end(data)
        print(type(data))

app = Flask(__name__)

@app.route("/newsite")
def showcontent():
    return render_template("html/destination.html")

@app.route("/getsearchInfo", methods = ["POST"])
def searchingSite():
    data = getInformation()
    dataSearching = request.form.get("searchingaction")
    print(dataSearching)
    print(f"the data is: {data}")
    print(type(data))
    return render_template("html/search.html", searchResults=returnedSearch(data, dataSearching))

@app.route("/openPage")
def openP():
    return render_template("html/search.html")



@app.route("/")
def showSite():
    color1 = random.randint(1, 255)
    color2 = random.randint(1, 255)
    color3 = random.randint(1, 255)
    return render_template("html/buttons.html", color1 = color1, color2 = color2, color3 = color3)

def getInformation():
    f = open("templates/html/search.html")
    #print(f.read())
    global readyData
    parser = overriddenHTMLParser()
    parser.feed(f.read())
    data = readyData
    print(data)
    #searchingSite(data)
    return data

def returnedSearch(data, toSearch):
    stringedData = ""
    for word in data:
        stringedData+=word + " "
    if stringedData.find(toSearch) != -1:
        dataWords = stringedData.split()
        answerWords = set()
        for i in dataWords:
            if toSearch in i:
                answerWords.add(i)
        answerString = ""
        for word in answerWords:
            answerString+=word + " "
        return f"The words are: {answerString}"
    else:
        return "No such data has been found"

if __name__ == "__main__":
    getInformation()
    app.run(host="0.0.0.0", port=5000) 