# coding : utf-8

import RPi.GPIO as GPIO

KEYPADlist = [4,23,18,17,27,22,24]

def KeypadRead():
	keypadnum = -1
	for i in range(7):
		if(not GPIO.input(KEYPADlist[i])):
			keypadnum = i
			break
	return keypadnum

GPIO.setmode(GPIO.BCM)

def init():
	for i in KEYPADlist:
		GPIO.setup(i, GPIO.IN)

def read():
	keypadnum = KeypadRead()
	return keypadnum

