import RPi.GPIO as gg
import time

gg.setmode(gg.BCM)
dac = [10, 9, 11, 5, 6, 13, 19, 26]
gg.setup(dac, gg.OUT)

def ten2bin(given_number):
    return [int(i) for i in bin(given_number)[2:].zfill(8)]

try:
    period = float(input())
    while True:
        for i in range(256):
            gg.output(dac, ten2bin(i))
            time.sleep(period)
finally:
    gg.output(dac, [0]*8)
    gg.cleanup()