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





C = Car(123,12313,10)
print('engine1 = ',C.engine)
C.set_engine('Toyota')
print('fuel = ',C.fuel)
print('weight = ',C.weight)
print('fuel_consumption = ',C.fuel_consumption)
print('engine2 = ',C.engine)

print(isinstance(C,Vehicle))