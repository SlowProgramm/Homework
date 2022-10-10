"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self,max_cargo):
        self.max_cargo = max_cargo

    def loadcargo(self, num):
        if (self.cargo + num) <= self.max_cargo:
            self.cargo = self.cargo + num
        else:
            raise Exception("CargoOverload")

    def remove_all_cargo(self):
        oldCargo, self.cargo = self.cargo, 0
        return oldCargo

    def __str__(self):
        return f"cargo = {self.cargo} max_cargo = {self.max_cargo}"
