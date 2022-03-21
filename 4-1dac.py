import RPi.GPIO as gg

gg.setmode(gg.BCM)
dac = [10, 9, 11, 5, 6, 13, 19, 26]
gg.setup(dac, gg.OUT)

def ten2bin(given_number):
    return [int(i) for i in bin(given_number)[2:].zfill(8)]

try:
    while True:
        inputt = input()
        if inputt == "q":
            break
        if inputt[1:].isnumeric() and (inputt[0].isnumeric() or ord(inputt[0]) == 45):
            inputt = int(inputt)
            if inputt >= 0:
                if inputt <= 255:
                    a = ten2bin(inputt)
                    gg.output(dac, a)
                    print((inputt * 3.3)/256)
                else:
                    print("ARE YOU STUPID? NUMBER CAN'T BE BIGER THAN 255!!!")
            else:
                    print("NOT POSITIVE!!! HOW DARE YOU")
        else:
            print("NOT NUM OR INT!!! HOW DARE YOU!")

finally:
    gg.output(dac, [0]*8)
    gg.cleanup()
