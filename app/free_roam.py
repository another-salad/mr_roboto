"""Will attempt to free roam around an area, avoiding collisions on the way"""

import sys
from time import sleep

from common.distance import Sight
from common.motors import motors


class Judgement:

    too_close = 100

    def __init__(self):
        self.sensor = Sight()
        self.motors = motors

    def set_position(self):
        """Tries to find a startable position"""
        attempts = 30
        for _ in range(attempts):
            if self.sensor.distance >= 200:
                return True

            self.motors.left(speed=0.8)
            sleep(0.1)

        return False

    def roam(self, speed=0.6):
        """Moves, stops on collision avoidance"""
        while True:
            can_move = self.set_position()
            if not can_move:
                break
            self.motors.forward(speed)
            while self.sensor.distance > self.too_close:
                sleep(0.05)
            self.motors.stop()

    def __call__(self):
        self.roam()

if __name__ == "__main__":
    move = Judgement()
    move()
