# coding : utf-8

import wiringpi as wp
import time

CS_MCP3208 = 8
SPI_CHANNEL = 0
SPI_SPEED = 1000000

def ReadMcp3208ADC(adcChannel):
	nAdcValue = 0
	
	wp.digitalWrite(CS_MCP3208, 0)
	retlen, retdata = wp.wiringPiSPIDataRW(SPI_CHANNEL, bytes([6,0,0]))
	r1 = retdata[1]
	r1 = 0x0F & r1
	nAdcValue = (r1 << 8) | retdata[2]
	wp.digitalWrite(CS_MCP3208, 1)
	return nAdcValue

# main
nCdsChannel = 0
nPhotoCellChannel = 1
nCdsValue = 0
nPhotoCellValue = 0

wp.wiringPiSetupGpio()
wp.wiringPiSPISetup(SPI_CHANNEL, SPI_SPEED)
wp.pinMode(CS_MCP3208, wp.OUTPUT)

while True:
	nCdsValue = ReadMcp3208ADC(nCdsChannel)
	print('LIGHT = %d Lux' % nCdsValue)
	time.sleep(0.5)

