#!/usr/bin/env python
########################################################################
# Filename    : SensorReading
# Description : Gets Avgerage Temperature and pH, Also gets Date of reading
# Author      : Anna Byrne
# modification: 2022/03/23
########################################################################
from TemperatureSensor import *
from pHsensor import *
import datetime
import time


def getAvg(numb): #numb is the number of times it will Read before averaging
    Error = 0
    setup()
    TempTotal=0
    pHTotal=0
    timepoint = datetime.datetime.now()
    for i in range(numb):
        #get temp
        Temp = read_temp()
        if type(Temp) == str:
            Error += 1
        #print(Temp)
        #get pH
        pH = read_pH()
        if type(pH) == str:
            Error += 10
        #print(pH)
        
        if Error > 0:
            if Error > 10:
                return "null","null",timepoint
            elif Error == 10:
                return "null",pH,timepoint
            else:
                return Temp,"null",timepoint
        TempTotal+=Temp
        pHTotal += pH
        
    AvgTemp= TempTotal/numb
    AvgTemp= round(AvgTemp,2)
    AvgpH= pHTotal/numb
    AvgpH= round(AvgpH,2)
    #get datetime
    timepassed = (datetime.datetime.now() - timepoint).total_seconds()
    #print(timepassed)
    #print(time.strftime("%d/%m/%y@%H:%M:%S"))
    #print("Temp:",AvgTemp,"pH:",AvgpH)
    timepoint = datetime.datetime.now()
    #print(timepoint)
    return AvgTemp, AvgpH, timepoint

#print(getAvg(20))