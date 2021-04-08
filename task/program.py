from json_functions import writeToJson,readFromJson
import math

# constant variables:
peopleCount = 100
experimentPerPerson = 10000
path = "input_param.json"
firstDay = 0
firstHour = 0
lastHour = 0
measuringDuration = 0 
interval = 0
solution = {}
daysAtWeek = ["Sunday","Monday","Tuesday","Wednesday","Thursday"]

def getEricData():
    data = readFromJson(path)
    firstDay = data["first working day"]
    firstHour = data["first hour"]
    lastHour = data["last hour"]
    measuringDuration = data["duration of one measuring"]
    interval = data["interval between measurements"]
    return firstDay,firstHour,lastHour,measuringDuration,interval

def getMinutesPerDay(firstHour,lastHour):
    print(((int(lastHour.split(":")[0]) + (int(lastHour.split(":")[1])/60))  - (int(firstHour.split(":")[0]) + (int(firstHour.split(":")[1])/60)))*60)
    print((int(lastHour.split(":")[0])*60 + int(lastHour.split(":")[1]))  - (int(firstHour.split(":")[0])*60 + int(firstHour.split(":")[1])))

    return ((int(lastHour.split(":")[0]) + (int(lastHour.split(":")[1])/60))  - (int(firstHour.split(":")[0]) + (int(firstHour.split(":")[1])/60)))*60

def doSchedule(firstDay,minutesPerDay,measuringDuration,interval):
    print("we are preparing your schedule' please wait")
    cycle = math.ceil(interval/measuringDuration) + 1 
    currentPerson = 1
    status = readFromJson("status.json")
    currentDay = firstDay
    currentMinute = 0
    currentWeek = 1
    queue = []
    for i in range(1,peopleCount+1):
        if status[str(i)] == 0:
            currentPerson += 1
        else: 
            break
    for i in range(currentPerson,currentPerson+cycle):
        if str(i) not in status:
            break
        queue.append(status[str(i)])
    queueCounter = 0
    flag = 1
    while len(queue) != 0:
        if currentDay == 6:
            currentDay = 1
            currentWeek += 1
        scheduleThisDay = []
        currentMinute = 0
        # checking if there is enough time for more measuring this day
        while currentMinute <= minutesPerDay - measuringDuration: 
            if peopleCount - currentPerson  == cycle and flag:
                for i in range(currentPerson+cycle,peopleCount):
                    queue.append(status[str(i)])
                flag = 0
            if len(queue) == 0:
                break
            if queueCounter == len(queue):
                queueCounter = 0
            queue[queueCounter] -= 1
            scheduleThisDay.append(currentPerson + queueCounter)
            currentMinute += measuringDuration
            if queue[queueCounter] == 0:
                if flag:
                    del status[str(currentPerson)]
                if str(currentPerson + cycle) in status:
                    queue.append(status[str(currentPerson + cycle)])
                queue.pop(0)
                currentPerson += 1
            else: 
                queueCounter += 1          
        solution[str(daysAtWeek[currentDay-1]) + str(currentWeek)] = scheduleThisDay
        currentDay += 1
        
def writeScheduleToFiles():
    writeToJson("schedule.json",solution)
         
def run():
    firstDay,firstHour,lastHour,measuringDuration,interval = getEricData()
    minutesPerDay = getMinutesPerDay(firstHour,lastHour)
    doSchedule(int(firstDay),minutesPerDay,float(measuringDuration),float(interval))
    writeScheduleToFiles()
    print("ready, enjoy it!")

