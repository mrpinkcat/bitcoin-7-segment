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
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 1)
        GPIO.output(DP, 1)
    if num == 1:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 1)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 1)
        GPIO.output(E, 1)
        GPIO.output(F, 1)
        GPIO.output(G, 1)
        GPIO.output(DP, 1)
    if num == 2:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 1)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 1)
        GPIO.output(G, 0)
        GPIO.output(DP, 1)
    if num == 3:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 1)
        GPIO.output(F, 1)
        GPIO.output(G, 0)
        GPIO.output(DP, 1)
    if num == 4:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 1)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 1)
        GPIO.output(E, 1)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        GPIO.output(DP, 1)
    if num == 5:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 0)
        GPIO.output(B, 1)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 1)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        GPIO.output(DP, 1)
    if num == 6:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 0)
        GPIO.output(B, 1)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        GPIO.output(DP, 1)
    if num == 7:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 1)
        GPIO.output(E, 1)
        GPIO.output(F, 1)
        GPIO.output(G, 1)
        GPIO.output(DP, 1)
    if num == 8:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        GPIO.output(DP, 1)
    if num == 9:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 1)
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 1)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        GPIO.output(DP, 1)
    pass

displayNum(0)
time.sleep(3)
displayNum(1)
time.sleep(3)
displayNum(2)
time.sleep(3)
displayNum(3)
time.sleep(3)
displayNum(4)
time.sleep(3)
displayNum(5)
time.sleep(3)
displayNum(6)
time.sleep(3)
displayNum(7)
time.sleep(3)
displayNum(8)
time.sleep(3)
displayNum(9)
time.sleep(3)
GPIO.cleanup()
