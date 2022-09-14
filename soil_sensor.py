from machine import Pin, ADC
import utime

'''
Code Notes

Add light vs deep sleep vs pushToCheck options
Add C++ Notes
'''


# initialize vars
led_onboard = Pin(25, Pin.OUT)
led_external = Pin(15, Pin.OUT, Pin.PULL_DOWN)
moisture_sensor = ADC(28)
conversion_factor = 3.3/65535

# primary application loop
while True:
    # onboard lights up when we read
    led_onboard.value(1)

    # check the sensor
    sensor_reading = moisture_sensor.read_u16()
    converted_reading = sensor_reading * conversion_factor
    print(converted_reading)

    # if below threshold, turn on water indicator
    if converted_reading > 1.4:
        led_external.value (1)
    else:
        led_external.value(0)

    # wait one second and then reset the led
    utime.sleep(1)
    led_onboard.value(0)
    utime.sleep(1) 

