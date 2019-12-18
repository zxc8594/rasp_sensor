# coding : utf-8

import wiringpi as wp
from time import sleep

CS_MCP3208 = 8
SPI_CHANNEL = 0
SPI_SPEED = 1000000

def init():
	wp.wiringPiSetupGpio()
	wp.wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED)
	wp.pinMode(CS_MCP3208, wp.OUTPUT)

def read():
	nAdcValue = 0
	
	wp.digitalWrite(CS_MCP3208, 0)
	retlen, retdata = wp.wiringPiSPIDataRW(SPI_CHANNEL, bytes([6,0,0]))
	r1 = retdata[1]
	r1 = 0x0F & r1
	nAdcValue = (r1 << 8) | retdata[2]
	wp.digitalWrite(CS_MCP3208, 1)
	return nAdcValue

