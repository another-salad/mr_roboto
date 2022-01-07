"""Tests that pigpio can be set"""

from time import sleep
from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory

###############################################################################
# You'll want to install pigpio via apt and make sure it is added to startup: #
#                                                                             #
# sudo systemctl enable pigpiod                                               #
# sudo systemctl start pigpiod                                                #
###############################################################################

if __name__ == "__main__":
    # Define GPIO pins to use on the Pi
    pintrigger = 17
    pinecho = 18
    sensor = DistanceSensor(echo=pinecho, trigger=pintrigger, pin_factory=PiGPIOFactory())
    print("Will now take 10 Ultrasonic measurements")
    for _ in range(10):
        print("Distance: %.1f cm" % (sensor.distance * 100))
        sleep(0.5)
