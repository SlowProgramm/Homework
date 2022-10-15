from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload
from dataclasses import dataclass

class Vehicle(ABC):
    weight = 0
    started = False
    fuel = 0
    fuel_consumption = 0

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        # if self.weight == weight and self.fuel_consumption == fuel_consumption and self.fuel == fuel:
        #   print('They are the same')

    def start(self):
        if self.started == False:  # Если
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError()
        elif self.started == True:
            if self.fuel <= 0:
                raise LowFuelError()
            elif self.fuel > 0:
                self.started = True

    def move(self, way):
        if self.fuel <= 0:
            raise NotEnoughFuel()
        elif self.fuel > 0:
            if self.fuel < self.fuel_consumption:
                raise NotEnoughFuel()
            elif self.fuel >= self.fuel_consumption:
                max_distance = self.fuel / self.fuel_consumption
                if max_distance >= way:
                    self.fuel = self.fuel - way * self.fuel_consumption
                elif max_distance < way:
                    raise NotEnoughFuel()

