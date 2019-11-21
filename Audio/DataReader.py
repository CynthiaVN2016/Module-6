import time 
import subprocess 
import os
import sys
import json

cabinetPID = None
doorPID = None
fridgePID = None
microwavePID = None 

path = "./Scripts/"

for line in sys.stdin:
	if (len(line) > 0):
		sensorData = json.loads(line)
		if ("msg" in sensorData) :
            process = None
			msg = sensorData["msg"]
			if (msg == "Open") : # related to the cabinet 
                cabinetPID = startProcess("cabinetScript.sh")
			elif (msg == "Closed") :
                killProcess(cabinetPID)
                cabinetPID = None
            elif (msg == "On") : # related to the microwave
                microwavePID = startProcess("microwaveScript.sh")
            elif (msg == "Off") :
                killProcess(microwavePID)
                microwavePID = None 
            elif (msg == "IN") : # related to the door
                doorPID = startProcess("doorScript.sh")
            elif (msg == "OUT") :
                killProcess(doorPID)
                doorPID = None
            elif (msg == "Touched"): # related to the fridge
                fridgePID = startProcess("fridgeScript.sh")
            elif (msg == "Released"):
                killProcess(fridgePID)
                fridgePID = None

def startProcess(scriptName):
    process = subprocess.Popen(path + scriptName)
    return process.pid

def killProcess(pid): 
    subprocess.Popen(path + "killScript.sh", pid)

			 
