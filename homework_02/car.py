from homework_02.base import Vehicle
"""
создайте класс `Car`, наследник `Vehicle`
"""

class Car(Vehicle):
    engine = None
    def set_engine(self, Engine):
        self.engine = str(Engine)
        print(self.fuel)
'''
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
'''




