#GND = 1
#3.3V = 0

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

A = 21
B = 20
C = 26
D = 16
E = 19
F = 13
G = 12
DP = 6
segments = (A, B, C, D, E, F, G, DP)

digit1 = 25
digit2 = 24
digit3 = 23
digit4 = 22
digits = (digit1, digit2, digit3, digit4)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 1)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)

#core

def displayNum(num):
    if num == 0:
        toDisplay = (0, 0, 0, 0, 0, 0, 1, 0)
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 1)
        GPIO.output(DP, 1)
    pass

displayNum(0)
time.sleep(3)
GPIO.cleanup()
