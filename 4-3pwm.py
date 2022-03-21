import RPi.GPIO as gg

gg.setmode(gg.BCM)
gg.setup(2, gg.OUT)
gg.setup(21, gg.OUT)
pwm = gg.PWM(2, 1000)
pwm.start(0)

try:
    while True:
        pwm.ChangeDutyCycle(int(input()))

finally:
    gg.output(2, 0)
    gg.cleanup()
