#Add Phidgets library
from Phidget22.Phidget import *
from Phidget22.Devices.TemperatureSensor import *
from Phidget22.Devices.PressureSensor import *
#Required for sleep statement
import time

#Create
temperatureSensor = TemperatureSensor()
pressureSensor = PressureSensor()

#Open
temperatureSensor.openWaitForAttachment(1000)
pressureSensor.openWaitForAttachment(1000)

#Create data file
outfile = open("data.csv", "w")
outfile.write("Date,Temperature,Pressure")

#Record data points
count = 0

#Use your Phidgets
while (True):
    #Update user
    print("Logging data...")
    
    #Write data to file in CSV format
    outfile.write(time.strftime("%Y-%m-%d %H:%M:%S") + "," + 
                  str(temperatureSensor.getTemperature()) + "," +
                  str(pressureSensor.getPressure()) + "\n")
    
    #Increment count
    count += 1
    
    #If 10 data points have been recorded, close file and exit program
    if(count == 10):
        outfile.close()
        print("Logging complete, exiting program")
        exit()
    
    time.sleep(1.0)
