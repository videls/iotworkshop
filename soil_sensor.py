from machine import Pin, ADC
import utime

'''
Code Notes

Add External LED as an option
Add conversion factor(3.3/65535)
Add light vs deep sleep vs pushToCheck options
Add C++ Notes
'''


# initialize vars
moisture_sensor = ADC(28)

# primary application loop
while True:
    print(moisture_sensor.read_u16())
    utime.sleep(1)
