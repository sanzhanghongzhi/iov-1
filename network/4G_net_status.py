#!/usr/bin/python

import serial
import time
import sys


ser=serial.Serial('/dev/ttyUSB1', baudrate=115200, timeout=.1, rtscts=0)

ser.write(b'ATE1\r')
#time.sleep(1)
response = ser.read(256)
print response

ser.write(b'AT^SYSINFO\r')
#time.sleep(1)
response = ser.read(256)
print response

ser.write(b'AT+CSQ\r')
#time.sleep(1)
response = ser.read(256)
print response

ser.write(b'AT+ZRSSI\r')
#time.sleep(1)
response = ser.read(256)
print response

ser.write(b'AT+ZSINR\r')
#time.sleep(1)
response = ser.read(256)
print response
