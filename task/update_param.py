import json
path = "input_param.json"
from json_functions import writeToJson,readFromJson

def setFirstWorkingDay(input):
    data = readFromJson()
    data["first working day"] = str(input)
    writeToJson(data)

def setFirstWorkingDay(input):
    data = readFromJson(path)
    data["first working day"] = str(input)
    writeToJson(path,data)

def setFirstHour(input1,input2):
    data = readFromJson(path)
    data["first hour"] = str(input1) + ":" + str(input2)
    writeToJson(path,data)

def setLastHour(input1,input2):
    data = readFromJson(path)
    data["last hour"] = str(input1) + ":" + str(input2)
    writeToJson(path,data)

def setMeasuringDuration(input):
    data = readFromJson(path)
    data["duration of one measuring"] = str(input)
    writeToJson(path,data)

def setInterval(input):
    data = readFromJson(path)
    data["interval between measurements"] = str(input)
    writeToJson(path,data)

def updateStatus(personNumber,status):
    data = readFromJson("status.json")
    data[personNumber] = int(status)
    writeToJson("status.json",data)



