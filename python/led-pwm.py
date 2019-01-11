import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
p = GPIO.PWM(18,50)


try:
        print("Iniciando...\nPressione CRTL-C para parar.")
        p.start(0)
        i=0.0
        while True:
            i = int(input("\nPercentual do Duty Cycle?"))
            p.ChangeDutyCycle(i)
                
except KeyboardInterrupt:
        pass
        print("Parando...")
        p.stop()
        GPIO.output(18, False)
