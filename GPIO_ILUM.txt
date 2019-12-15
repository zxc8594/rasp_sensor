# coding : utf-8

import RPi.GPIO as GPIO
import time

CS_MCP3208 = 8
SPI_CHANNEL = 0
SPI_SPEED = 1000000

def ReadMcp3208ADC(adcChannel):
	nAdcValue = 0
	buff[0] = 0x06 | ((adcChannel & 0x07) >> 2)

# main
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
