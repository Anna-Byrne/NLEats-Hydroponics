#!/usr/bin/env python
########################################################################
# Filename    : SensorReading
# Description : Read Sensors and date and sends ino firebase every 15mins
# Author      : Anna Byrne
# modification: 2022/04/13
########################################################################
from SensorReading import*
from FirebaseSetup import*


def main():
    TempRange = [10,25] #this will become the Pi reading the ID for the Temperature and pH Ranges
    pHrange = [6,8]

    Reading= getAvg(20)
    temp = Reading[0]
    pH = Reading[1]
    datetime = Reading[2]
    

    # Out of Range for temp and pH that will determine the Email sent (not in use)
    if type(temp) == str:
        AlertOwner = True
        print("Temperautrue Sensor Issuse")
    elif TempRange[0] > temp or temp > TempRange[1]:
        print("error out of temp range")
        outRangeT = 1
        #update alert feild and send email based on temp to user
    else:
        outRangeT = 0
    
    if type(pH) == str:
        AlertOwner = True
        print("pH Sensor Issuse")
    elif pHrange[0] > pH or pH > pHrange[1]:
        print("error out of pH reange") 
        outRangep = 1
        #update alert feild and send email based on temp to user
    else:
        outRangep = 0
    
    #Update Alert to System (not in Use)
    # if outRangep == 1 or outRangeT ==1:
    #     AlertOwner = True
    # else:
    #     AlertOwner = False

    #send data to fiebase
    print("Date:",datetime, "Temperature:", temp,"pH:",pH)
    data = {
        u'Temp': temp,
        u'pH': pH,
        u'Date':datetime,
        u'OID':UserID,
        u'SID':SysID
    }
    
    db.collection(u'Readings').add(data)


    #Add an alert field in the system ID and have it update based on (make a new file for this)


main()