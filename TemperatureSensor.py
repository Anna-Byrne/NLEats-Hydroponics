#!/usr/bin/env python
########################################################################
# Filename    : TemperatureSensor.py
# Description : Gets Temperature Reading in C
# Author      : Anna Byrne
# modification: 2022/04/18
########################################################################
import os
import glob
import time
import datetime

def read_temp(decimals = 1):

    """Reads the temperature from a 1-wire device"""
    try:
        device = glob.glob("/sys/bus/w1/devices/" + "28*")[0] + "/w1_slave"
    except IndexError:
        print("TemperaureSensor is dicsoncected")
        return("Sensor Down")
    
    with open(device, "r") as f:
            lines = f.readlines()
    while lines[0].strip()[-3:] != "YES":
        lines = read_temp_raw()
    equals_pos = lines[1].find("t=")
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp = round(float(temp_string) / 1000.0, decimals)
    return float(temp)

read_temp()