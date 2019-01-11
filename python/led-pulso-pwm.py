import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18,100)


try:
        print("Iniciando...\nPressione CRTL-C para parar.")
        p.start(0)
        while True:
            for i in range(1,100,2):
                p.ChangeDutyCycle(i)
                time.sleep(0.5/i)
            for i in range(100,1,-2):
                p.ChangeDutyCycle(i)
                time.sleep(0.5/i)
                
except KeyboardInterrupt:
        pass
        print("Parando...")
        p.stop()
        GPIO.output(18, False)
