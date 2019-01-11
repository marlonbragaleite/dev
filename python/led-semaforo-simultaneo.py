import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


try:
        print("Iniciando...\nPressione CRTL-C para parar.")
        while True:
                GPIO.output(18, True)
                time.sleep(1)
        
                GPIO.output(23, True)
                time.sleep(1)

                GPIO.output(24, True)
                time.sleep(1)

                GPIO.output(18, False)
                time.sleep(1)
        
                GPIO.output(23, False)
                time.sleep(1)

                GPIO.output(24, False)
                time.sleep(1)

except KeyboardInterrupt:
        pass
        print("Parando...")
        GPIO.output(18, False)
        GPIO.output(23, False)
        GPIO.output(24, False)
