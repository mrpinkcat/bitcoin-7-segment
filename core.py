#GND = 1
#3.3V = 0

import RPi.GPIO as GPIO
import time
import requests
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
    pass

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 0)
    pass

#core

def displayNum(num, digit):
    if digit == 1:
        GPIO.output(digit1, 1)
        GPIO.output(digit2, 0)
        GPIO.output(digit3, 0)
        GPIO.output(digit4, 0)
        GPIO.output(DP, 1)
        pass
    if digit == 2:
        GPIO.output(digit1, 0)
        GPIO.output(digit2, 1)
        GPIO.output(digit3, 0)
        GPIO.output(digit4, 0)
        GPIO.output(DP, 1)
        pass
    if digit == 3:
        GPIO.output(digit1, 0)
        GPIO.output(digit2, 0)
        GPIO.output(digit3, 1)
        GPIO.output(digit4, 0)
        GPIO.output(DP, 0)
        pass
    if digit == 4:
        GPIO.output(digit1, 0)
        GPIO.output(digit2, 0)
        GPIO.output(digit3, 0)
        GPIO.output(digit4, 1)
        GPIO.output(DP, 1)
        pass

    if num == 0:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 1)
        pass
    if num == 1:
        GPIO.output(A, 1)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 1)
        GPIO.output(E, 1)
        GPIO.output(F, 1)
        GPIO.output(G, 1)
        pass
    if num == 2:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 1)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 1)
        GPIO.output(G, 0)
        pass
    if num == 3:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 1)
        GPIO.output(F, 1)
        GPIO.output(G, 0)
        pass
    if num == 4:
        GPIO.output(A, 1)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 1)
        GPIO.output(E, 1)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        pass
    if num == 5:
        GPIO.output(A, 0)
        GPIO.output(B, 1)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 1)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        pass
    if num == 6:
        GPIO.output(A, 0)
        GPIO.output(B, 1)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        pass
    if num == 7:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 1)
        GPIO.output(E, 1)
        GPIO.output(F, 1)
        GPIO.output(G, 1)
        pass
    if num == 8:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 0)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        pass
    if num == 9:
        GPIO.output(A, 0)
        GPIO.output(B, 0)
        GPIO.output(C, 0)
        GPIO.output(D, 0)
        GPIO.output(E, 1)
        GPIO.output(F, 0)
        GPIO.output(G, 0)
        pass
    pass

while True:
    loop = 0
    r = requests.get("https://api.coinbase.com/v2/prices/spot?currency=USD")
    price = r.json()['data']['amount'].replace(".", "")
    while loop != 30000:
        digit = 0
        while digit < len(price):
            digitToDisplay = digit + 1
            displayNum(int(price[digit]), digitToDisplay)
            time.sleep(0.001)
            digit += 1
            pass
        pass
    pass

GPIO.cleanup()
