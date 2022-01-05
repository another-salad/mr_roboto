"""Tests moving forward and backwards"""

from time import sleep
from gpiozero import CamJamKitRobot

if __name__ == "__main__":
    roboto = CamJamKitRobot()
    for _ in range(5):
        for x in [{"curve_left": 0.3}, {"curve_right": 0.6}]:
            roboto.forward(speed=0.4, **x)
            sleep(0.5)
            roboto.reverse()
            sleep(0.5)
