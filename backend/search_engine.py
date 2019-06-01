import json
import csv


def getFile(source):
    with open(source) as json_file:
        data = json.load(json_file)
        return data


def getFrance():
    file = getFile('resources/data_fr.json')
    return file


def getSpain():
    file = getFile('resources/data_es.json')
    return file


def getUK():
    file = getFile('resources/data_uk.json')
    return file


def applySearch(product, country):
    listOfCoincidences = {}
    data = ""
    if country.lower() == "Spain".lower():
        data = getSpain()
    elif country.lower() == "United Kingdom".lower():
        data = getUK()
    elif country.lower() == "France".lower():
        data = getFrance()
    for pair in data:
        if product.lower() in data[pair].lower():
            cleanProduct = product
            cleanProduct.replace("\n", "")
            listOfCoincidences[pair] = data[pair]
    return listOfCoincidences


def searchEU(product):
    savedIDs = []
    codeDescription = {}
    with open('resources/nomen_en.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if str(product).lower() in row["description"].lower() or row["pid"] in savedIDs:
                savedIDs.append(row["id"])
                codeDescription[row["code"]] = row["description"]
        return codeDescription