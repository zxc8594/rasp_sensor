# coding : utf-8

import RPi.GPIO as GPIO
import time

KEYPADlist = [4,23,18,17,27,22]

def KeypadRead():
	keypadnum = -1
	for i in range(6):
		if(not GPIO.input(KEYPADlist[i])):
			keypadnum = i
			break
	return keypadnum

GPIO.setmode(GPIO.BCM)

for i in KEYPADlist:
	GPIO.setup(i, GPIO.IN)
time.sleep(0.5)

# main
while(1):
	try:
		keypadnum = KeypadRead()
		if keypadnum != -1:
			print(keypadnum)
			time.sleep(0.2)
	except KeyboardInterrupt:
		pass
	time.sleep(0.1)
GPIO.cleanup()
