# coding : utf-8

import RPi.GPIO as GPIO
from time import sleep
from math import floor

SCK = 6
SDA = 12

TEMP = 0
HUMI = 1

NOACK = 0
ACK = 1

SHT11_humi = 0
SHT11_temp = 0
checksum = 0

val_humi = 0
val_temp = 0

MEASURE_TEMP = 0x03
MEASURE_HUMI = 0x05
READ_STATUS_REG = 0x07
WRITE_STATUS_REG = 0x06
RESET = 0x1e

def init():
	GPIO.setup(SDA, GPIO.OUT)
	GPIO.setup(SCK, GPIO.OUT)
	Connection_reset()

def Connection_reset():
	GPIO.output(SDA, 1)
	GPIO.output(SCK, 0)
	for i in range(0, 9):
		GPIO.output(SCK, 1)
		sleep(0.001)
		GPIO.output(SCK, 0)
		sleep(0.001)

def Transmission_start():
	GPIO.output(SDA, 1)
	GPIO.output(SCK, 0)
	sleep(0.001)
	GPIO.output(SCK, 1)
	sleep(0.001)
	GPIO.output(SDA, 0)
	sleep(0.001)
	GPIO.output(SCK, 0)
	sleep(0.001)
	GPIO.output(SCK, 1)
	sleep(0.001)
	GPIO.output(SDA, 1)
	sleep(0.001)
	GPIO.output(SCK, 0)

def get_SHT11_data(type):
	err = 0
	if type == HUMI:
		err += Measure(HUMI)
		if err != 0:
			Connection_reset()
		else:
			calc_SHT11(SHT11_humi, SHT11_temp)
		return val_humi
	elif type == TEMP:
		err += Measure(TEMP)
		if err != 0:
			Connection_reset()
		else:
			calc_SHT11(SHT11_humi, SHT11_temp)
		return val_temp
	else:
		return 0

def Measure(mode):
	err = 0
	if mode == TEMP:
		err += Write_byte(MEASURE_TEMP)
	elif mode == HUMI:
		err += Write_byte(MEASURE_HUMI)
	if err != 0:
		return err
	GPIO.setup(SDA, GPIO.IN)
	while(GPIO.input(SDA)):
		pass
	GPIO.setup(SDA, GPIO.IN)
	msb = Read_byte(ACK)
	lsb = Read_byte(ACK)
	
	global SHT11_temp
	global SHT11_humi
	global checksum
	
	if mode == TEMP:
		SHT11_temp = (msb * 256) + lsb
	elif mode == HUMI:
		SHT11_humi = (msb * 256) + lsb
	checksum = Read_byte(NOACK)
	return err

def Write_byte(value):
	err = 0
	GPIO.setup(SDA, GPIO.OUT)
	i = 0x80
	while i > 0:
		if i & value:
			GPIO.output(SDA, 1)
		else:
			GPIO.output(SDA, 0)
		sleep(0.001)
		GPIO.output(SCK, 1)
		sleep(0.001)
		GPIO.output(SCK, 0)
		sleep(0.001)
		i = floor(i/2)
	GPIO.output(SDA, 1)
	GPIO.setup(SDA, GPIO.IN)
	sleep(0.001)
	GPIO.output(SCK, 1)
	err = GPIO.input(SDA)
	GPIO.output(SCK, 0)
	GPIO.setup(SDA, GPIO.OUT)
	return err

def Read_byte(ack):
	val = 0
	GPIO.setup(SDA, GPIO.OUT)
	GPIO.output(SDA, 1)
	sleep(0.001)
	GPIO.setup(SDA, GPIO.IN)
	i = 0x80
	while i > 0:
		GPIO.output(SCK, 1)
		sleep(0.001)
		if GPIO.input(SDA):
			val = (val | i)
		GPIO.output(SCK, 0)
		sleep(0.001)
		i = floor(i/2)
	GPIO.setup(SDA, GPIO.OUT)
	if ack:
		GPIO.output(SDA, 0)
	else:
		GPIO.output(SDA, 1)
	GPIO.output(SCK, 1)
	sleep(0.001)
	GPIO.output(SCK, 0)
	sleep(0.001)
	GPIO.output(SDA, 1)
	return val

def calc_SHT11(humidity, temperature):
	C1 = -2.0468
	C2 = 0.0367
	C3 = -0.0000015955
	T1 = 0.01
	T2 = 0.00008
	rh = humidity
	t = temperature
	t_C = ((t * 0.01) - 40.1) - 5
	rh_lin = (C3 * rh * rh) + (C2 * rh) + C1
	rh_true = (t_C - 25) * (T1 + (T2 * rh)) + rh_lin
	
	if rh_true > 100:
		rh_true = 100
	if rh_true < 0.1:
		rh_true = 0.1
	
	global val_temp
	global val_humi
	
	val_temp = t_C
	val_humi = rh_true

def read():
	Transmission_start()
	temp = get_SHT11_data(TEMP)
	Transmission_start()
	humi = get_SHT11_data(HUMI)

	return temp, humi
	
#print('Temp = %.2f C, Humi = %.2f %%' % (temp, humi))
