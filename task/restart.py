from json_functions import writeToJson

peopleCount = 100
experimentPerPerson = 10000
path = "status.json"

def restarting():
    data = {}
    for i in range(1,peopleCount+1):
        data[str(i)] = experimentPerPerson
    writeToJson(path, data)
    

