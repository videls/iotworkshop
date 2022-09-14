from machine import Pin, ADC
import utime

# initialize vars
moisture_sensor = ADC(28)

# primary application loop
while True:
    print(moisture_sensor.read_u16())
    utime.sleep(1)
