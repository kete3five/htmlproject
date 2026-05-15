from flask import *
from pythonfilePro import *

app = Flask(__name__)

@app.route("/button")
def showinformationonClick():
    file = getDatafromAPI("bitcoin", "usd", "1", "hourly")
    data = translatingTohumanTime(unJSON(file))
    ansList = []
    for i  in range(len(data)):
        ansList.append(f"Bitcoin was estimated at {data[i][1]}$ at {data[i][0]}")
    print(ansList)
    return render_template("html/bitcoins.html", text = data)

@app.route("/")
def showinformationonClickupgraded():
    return render_template("html/bitcoins.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 
