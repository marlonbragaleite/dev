#!/usr/bin/python3.5
import RPi.GPIO as GPIO
import time
import menu

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

try:
	menu.additem(10,10," VERMELHO ")
	menu.additem(10,12,"  VERDE   ")
	menu.additem(10,14,"   AZUL   ")
	menu.additem(10,16,"   SAIR   ")
	menu.setcolor(1,2,3,4)
	item = 1
	#print("Iniciando...\nPressione CTRL-C para parar.")
	while item!=0:
		item = menu.runmenu(item,True)

		if item == 1:
			GPIO.output(18, True)
			time.sleep(1)
			GPIO.output(18, False)

		if item == 2:
			GPIO.output(23, True)
			time.sleep(1)
			GPIO.output(23, False)

		if item == 3:
			GPIO.output(24, True)
			time.sleep(1)
			GPIO.output(24, False)
		if item == 4:
			item = 0
except KeyboardInterrupt:
	pass
print("Parando...")
GPIO.output(18, False)
GPIO.output(23, False)
GPIO.output(24, False)
