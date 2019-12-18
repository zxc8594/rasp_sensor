# coding : utf-8

import wiringpi as wp
from time import sleep

BUZZER_PIN = 11

#
scale = [523,587,659,698,784,880,987,1046,1174,1318,1396,1568]

HI_S = [9,7,9,7]
HI_D = [0.1,0.1,0.1,0.2]

COIN_S = [7,10]
COIN_D = [0.1,0.2]

DEATH_S = [5,4,3,2]
DEATH_D = [0.1,0.1,0.1,0.2]

WIN_S = [0,2,4,7]
WIN_D = [0.1,0.1,0.1,0.5]

SOUND_S = [HI_S,COIN_S,DEATH_S,WIN_S]
SOUND_D = [HI_D,COIN_D,DEATH_D,WIN_D]

def changeFreq(freq):
	wp.pwmWrite(BUZZER_PIN, freq)
	wp.softToneWrite(BUZZER_PIN, freq)

def stopFreq():
	wp.softToneWrite(BUZZER_PIN, 0)

def init():
	wp.wiringPiSetupGpio()
	wp.softToneCreate(BUZZER_PIN)
	stopFreq()

def play(mode):
	for i in range(len(SOUND_S[mode])):
		changeFreq(scale[SOUND_S[mode][i]])
		sleep(SOUND_D[mode][i])
		stopFreq()

