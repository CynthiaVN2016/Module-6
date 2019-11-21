import time 
import subprocess 
import os
import sys
import json

cabinetPID = None
doorPID = None
fridgePID = None
microwavePID = None 

path = "/home/pi/Desktop/Module-6/Audio/Scripts/"

def startProcess(scriptName):
    print("Calling " + scriptName)
    process = subprocess.Popen(path + scriptName, shell=False)
    return process.pid

def killProcess(pid):
    print("Killing Time: " + str(pid))
    subprocess.Popen([path + "killScript.sh", str(pid)])
    
for line in sys.stdin:
    if (len(line) > 0):
        try:
            sensorData = json.loads(line)
            print(sensorData)
            if ("msg" in sensorData) :
                msg = sensorData["msg"]
                print(msg)
                if (msg == "Open") : # related to the cabinet 
                    cabinetPID = startProcess("cabinetScript.sh")
                    print(cabinetPID)
                elif (msg == "Closed" and cabinetPID != None) :
                    print(cabinetPID)
                    print(os.getppid()) # Killing parent kills the entire thing, so no good
                    killProcess(cabinetPID)
                    cabinetPID = None
                elif (msg == "On") : # related to the microwave
                    microwavePID = startProcess("microwaveScript.sh")
                elif (msg == "Off" and microwavePID != None) :
                    killProcess(microwavePID)
                    microwavePID = None 
                elif (msg == "IN") : # related to the door
                    doorPID = startProcess("doorScript.sh")
                elif (msg == "OUT" and doorPID != None) :
                    killProcess(doorPID)
                    doorPID = None
                elif (msg == "Touched"): # related to the fridge
                    fridgePID = startProcess("fridgeScript.sh")
                elif (msg == "Released" and fridgePID != None):
                    killProcess(fridgePID)
                    fridgePID = None
        except ValueError:
            pass



             
