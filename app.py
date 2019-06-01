# Import expected headers we'll need
from flask import Flask, render_template, request, json
from flask_bootstrap import Bootstrap
from flask import send_file
import random
from glob import glob
import yaml

from backend.search_engine import *
from backend.language_processor import *
from resources import *


app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/initialSearch', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        userInput = request.form

        # Get user selection:
        productSelectedUser = userInput["product"]
        countryOrigin = userInput["countryOrigin"]
        countryDestination = userInput["countryDestination"]

        # Get regional legislation
        originReturnedDict = applySearch(userInput["product"], userInput["countryOrigin"])
        destinationReturnedDict = applySearch(userInput["product"], userInput["countryDestination"])

        # Get EU legislation
        EUlegislation = searchEU(userInput["product"])

        # Apply NLP to get definitions and synonyms
        listOfHelpWords = getHelpWords(userInput["product"])
        definingWords = getDefiningWords(userInput['product'])

        # Also search for the legislation of the synonyms in case the input word has few meanings:
        if len(definingWords) < 2:
            for element in listOfHelpWords:
                thisOrigin = applySearch(element, userInput["countryOrigin"])
                originReturnedDict = {**thisOrigin, **originReturnedDict}

                thisDestination = applySearch(element, userInput["countryDestination"])
                destinationReturnedDict = {**thisDestination, **originReturnedDict}

        return render_template("firstResult.html", userInput=userInput, originReturnedDict=originReturnedDict,
                               destinationReturnedDict=destinationReturnedDict, countryOrigin=countryOrigin,
                               countryDestination=countryDestination, EUlegislation=EUlegislation,
                               definingWords=definingWords, productSelectedUser=productSelectedUser)


@app.route('/compute/<file>', methods=['POST', 'GET'])
def signup(file):
    if request.method == 'POST' or request.method == 'GET':
        ubication = "resources/pdfs/" + file
        with open(ubication, 'rb'):
            return send_file(ubication, attachment_filename=ubication)


@app.route('/giveFeedBack', methods=['POST', 'GET'])
def giveFeedBack():
    if request.method == 'POST':
        userInput = request.form
        resultText = userInput["mainText"]
        cDestin = userInput["cDestin"]
        cOrigin = userInput["cOrigin"]
        pSel = userInput["pSel"]

        location = "jsons/"
        file_name = location + cDestin + cOrigin + pSel + str(random.randint(0, 50000)) + '.json'

        toPrint = {}
        toPrint["resultText"] = resultText
        toPrint["cDestin"] = cDestin
        toPrint["cOrigin"] = cOrigin
        toPrint["pSel"] = pSel

        with open(file_name, 'w') as outfile:
            json.dump(toPrint, outfile, ensure_ascii=False)

        allTexts = []
        allcDestin = []
        allcOrigin = []
        allPSel = []
        for f_name in glob(location + '*.json'):
            detect = True
            with open(f_name) as data_file:
                for bigelement in data_file:
                    if detect:
                        itsADictPre = bigelement
                        itsADict = {}
                        itsADict = yaml.load(itsADictPre)
                        allTexts.append(itsADict["resultText"])
                        allcDestin.append(itsADict["cDestin"])
                        allcOrigin.append(itsADict["cOrigin"])
                        allPSel.append(itsADict["pSel"])

        return render_template("showFeedBack.html", allPSel=allPSel, allTexts=allTexts,
                               allcOrigin=allcOrigin, allcDestin=allcDestin)


@app.route('/show/static-pdf/')
def show_static_pdf():
    with open('/path/of/file.pdf', 'rb') as static_file:
        return send_file(static_file, attachment_filename='file.pdf')


if __name__ == "__main__":
    app.run(host='0.0.0.0')