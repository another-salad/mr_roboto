"""Moves forward until sensor reading hits 50mm distance"""

from time import sleep

from common.distance import Sight
from common.motors import motors

if __name__ == "__main__":
    sensor = Sight()
    if sensor.distance > 300:
        print("Starting up")
        motors.forward(0.4)
        while sensor.distance > 100:
            sleep(0.1)
        print("Stopping")
        motors.stop()
    else:
        print("Too close to an object, give robot atleast 300mm of free forward space")
