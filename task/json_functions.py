import json
from os import close

def readFromJson(path):
    the_file = open(path)
    data = json.load(the_file)
    the_file.close()
    return data

def writeToJson(path, data):
    with open(path, "w") as the_file:
        json.dump(data, the_file)