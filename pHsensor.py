#!/usr/bin/env python
########################################################################
# Filename    : pHsensor.py
# Description : Gets pH reading
# Author      : Anna Byrne
# modification: 2022/03/23
# Notes       : This program is refernced ADC.py by Freenove
########################################################################
import os
import glob
import time
import datetime
import RPi.GPIO as GPIO
from ADCDevice import*

adc = ADCDevice() # Define an ADCDevice class object

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4a)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n")
        #pH sensor is not connceted/respoding/not in location specified
        return "pH sensor Issue"

def getpH(voltage):
    offset = 2.7
    pHvalue = 7+ (2.5-voltage)*offset
    pHvalue = round(pHvalue,2)
    return pHvalue

def read_pH():
    
    try:
        value = adc.analogRead(0)    # read the ADC value of channel 0
    except AttributeError:
        return
    voltage = value / 255.0 * 5  # calculate the voltage value
    pH = getpH(voltage)
    #print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
    return pH

