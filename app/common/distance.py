"""HR SC04 distance sensor object"""

from gpiozero import DistanceSensor
from gpiozero.pins.pigpio import PiGPIOFactory


class Sight(DistanceSensor):
    """A light wrap around DistanceSensor"""

    pintrigger = 17
    pinecho = 18

    def __init__(self):
        """init baby"""
        super().__init__(echo=self.pinecho, trigger=self.pintrigger, pin_factory=PiGPIOFactory())

    @property
    def distance(self):
        """Returns the distance from the sensor in mm"""
        return int(super().distance * 1000)
