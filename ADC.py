#!/usr/bin/env python3
########################################################################
# Filename    : ADC.py
# Description : Use ADC module to read the voltage value of potentiometer.
# Author      : www.freenove.com
# modification: 2020/03/06
########################################################################

#Note: This ADC chip (ADS7830) reads only 8bits so its next to impossible to keep a consitant reading for the pH
#

import time
from ADCDevice import *

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
        exit(-1)

# added so the pH sensor can be calibrated and for testing
def getpH(voltage):
    offset = 2.7
    pHvalue = 7+ (2.5-voltage)*offset
    pHvalue = round(pHvalue,2)
    return pHvalue

def loop():
    while True:
        value = adc.analogRead(0)    # read the ADC value of channel 0
        voltage = value / 255.0 * 5  # calculate the voltage value
        ph=getpH(voltage)
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        print(ph) #see final pH value
        time.sleep(0.1)

def destroy():
    adc.close()



if __name__ == '__main__':   # Program entrance
    print ('Program is starting ... ')
    try:
        setup()
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
        
    
