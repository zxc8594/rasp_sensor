# coding : utf-8

import RPi.GPIO as GPIO
import GPIO_KEYPAD
import GPIO_TEMPHUMI
import GPIO_ILUM
import GPIO_BUZZER
from time import sleep
from multiprocessing import Process, Queue

# initial values
KEYPAD_BUF = 1
TEMP_BUF = 1
HUMI_BUF = 1
ILUM_BUF = 1

# GPIO init
GPIO.setmode(GPIO.BCM)

# KEYPAD, TEMPHUMI, ILUM, BUZZER modules init
GPIO_KEYPAD.init()
GPIO_TEMPHUMI.init()
GPIO_ILUM.init()
GPIO_BUZZER.init()

# KEYPAD, TEMP|HUMI|ILUM Threads define
def getKeyThread(name, keyQ):
	while(1):
		keyQ.put(GPIO_KEYPAD.read())
		sleep(0.1)

def getTempHumiIlumThread(name, tempQ, humiQ, ilumQ):
	while(1):
		temp, humi = GPIO_TEMPHUMI.read()
		ilum = GPIO_ILUM.read()
		tempQ.get()
		humiQ.get()
		ilumQ.get()
		tempQ.put(temp)
		humiQ.put(humi)
		ilumQ.put(ilum)
		sleep(1)

# KEYPAD thread init
keyQ = Queue(KEYPAD_BUF)
keyT = Process(target=getKeyThread, args=('KT', keyQ))

# TEMP|HUMI|ILUM thread init
tempQ = Queue(TEMP_BUF)
humiQ = Queue(HUMI_BUF)
ilumQ = Queue(ILUM_BUF)
tempQ.put(-1)
humiQ.put(-1)
ilumQ.put(-1)
temphumiilumT = Process(target=getTempHumiIlumThread, args=('THT', tempQ, humiQ, ilumQ))

# all threads start
keyT.start()
temphumiilumT.start()

# main
while(1):
	key = keyQ.get()
	if key == 0:
		GPIO_BUZZER.play(0)
	elif key == 1:
		GPIO_BUZZER.play(1)
	elif key == 2:
		GPIO_BUZZER.play(2)
	elif key == 3:
		GPIO_BUZZER.play(3)
	elif key == 5:
		temp = tempQ.get()
		humi = humiQ.get()
		ilum = ilumQ.get()
		tempQ.put(temp)
		humiQ.put(humi)
		ilumQ.put(ilum)
		print(temp, humi, ilum)
	elif key == 6:
		print('face recognition')
