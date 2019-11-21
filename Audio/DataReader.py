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
			if (msg == "Open") :
                process = subprocess.Popen(path + "cabinetScript.sh")
                cabinetPID = process.pid 
			elif (msg == "Closed") :
                subprocess.Popen(path + "killScript.sh", cabinetPID)
                cabinetPID = None
            elif (msg == "On") :
                continue
            elif (msg == "Off") :
                continue
            elif (msg == "IN") :
                continue
            elif (msg == "OUT") :
                continue 
            elif (msg == "Touched"):
                continue
            elif (msg == "Released"):
                continue


			 
