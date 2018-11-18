from flask import Flask, request, render_template
from backend import *


def testfunc(origin, amorpm):
    print(origin + amorpm)


app = Flask(__name__)


@app.route('/')
def main():
    return render_template("main.html")

@app.route('/<origin>_to_<destination>_<departorarrive>_<date>_<time>_<amorpm>')
def gate(origin, destination, departorarrive, date, time, amorpm):

    #destination = destination[-3:]

    #callfunc
    dictionary = scrape(origin, destination, departorarrive, date, time, amorpm)

    #option 1 variables
    option1depart=dictionary["Depart1"]
    option1arrive=dictionary["Arrive1"]
    option1time=dictionary["TimeElapsed1"]
    option1price=dictionary["Price1"]

    # option 2 variables
    option2depart = dictionary["Depart2"]
    option2arrive = dictionary["Arrive2"]
    option2time = dictionary["TimeElapsed2"]
    option2price = dictionary["Price2"]

    # option 3 variables
    option3depart = dictionary["Depart3"]
    option3arrive = dictionary["Arrive3"]
    option3time = dictionary["TimeElapsed3"]
    option3price = dictionary["Price3"]

    return render_template("gate.html", origin=origin, destination=destination, departorarrive=departorarrive, date=date, time=time, amorpm=amorpm,
                           option1depart=option1depart, option1arrive=option1arrive, option1time=option1time,
                           option1price=option1price, option2depart=option2depart, option2arrive=option2arrive,
                           option2time=option2time, option2price=option2price, option3depart=option3depart,
                           option3arrive=option3arrive, option3time=option3time, option3price=option3price)

@app.route('/gatetest')
def gatetest():
    return render_template("gatetest.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")


if __name__ == "__main__":
    app.run(debug=True)