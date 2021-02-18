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

#Use your Phidgets
while (True):
    #Update user
    print("Logging data...")
    
    #Write data to file in CSV format
    with open ('var/www/data.csv','a') as datafile:
        datafile.write(time.strftime("%Y-%m-%d %H:%M:%S") + "," + 
                  str(temperatureSensor.getTemperature()) + "," +
                  str(pressureSensor.getPressure()) + "\n")
    
    time.sleep(1.0)
