from homework_02.base import Vehicle
"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.engine import Engine
#pytest testing/test_homework_02 -s -vv
class Car(Vehicle):
    engine = None
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    def set_engine(self, Engine):
        self.engine = Engine
        print(self.fuel)


'''
car = Car(0,0,0)

print(car)
'''

