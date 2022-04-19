#!/usr/bin/python3
from signal import signal, SIGTERM, SIGHUP, pause
from smbus import SMBus
import os
import glob
from time import sleep
import datetime
import RPi.GPIO as GPIO

bus= SMBus(1)

def safeExit(signnum, frame):
    exit(1)



ASD7830_commands = [0x84, 0xc4, 0x94, 0xd4, 0xa4, 0xe4, 0xb4, 0xf4] #A0-A7 in order

def read_ASD7830(input):
    bus.write_byte(0x4a, ASD7830_commands[input])
    return bus.read_byte(0x4a) # 4a is the id for this chip as I use it can change

def values(input):
    while True:
        value = read_ASD7830(input)
        print(value)
        sleep(1)

signal(SIGTERM, safeExit)
signal(SIGHUP, safeExit)

values(0)
