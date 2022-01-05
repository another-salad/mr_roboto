"""Validates the distance sensor setup"""

from time import sleep
from gpiozero import DistanceSensor

if __name__ == "__main__":
    # Define GPIO pins to use on the Pi
    pintrigger = 17
    pinecho = 18
    sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)
    print("Will now take 10 Ultrasonic measurements")
    for _ in range(10):
        print("Distance: %.1f cm" % (sensor.distance * 100))
        sleep(0.5)
