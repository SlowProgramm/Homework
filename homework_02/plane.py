from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle
'''
class Plane(Vehicle):
    cargo = 0
    max_cargo = 0

    def __init__(self,weight, fuel, fuel_consumption, max_cargo):
        self.max_cargo = max_cargo
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def load_cargo(self, num):
        if (self.cargo + num) <= self.max_cargo:
            self.cargo = self.cargo + num
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        oldCargo, self.cargo = self.cargo, 0
        return oldCargo
'''
