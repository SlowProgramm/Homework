from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel, CargoOverload

from dataclasses import dataclass

'''
pytest testing/test_homework_02 -s -vv
git remote add origin git@github.com:SlowProgramm/PythonBasic-Homework.git
git remote add origin https://github.com/SlowProgramm/PythonBasic-Homework.git
git branch -M master
git push -u origin master
'''


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
                elif max_distance < 0:
                    raise NotEnoughFuel()


C = Vehicle(100, 0,  10)
# with pytest.raises(LowFuelError) as exc_info:
#C.start()
'''
print('C.fuel = ' + str(C.fuel))
print('C.fuel_consumption = ' + str(C.fuel_consumption))
C.move(1000)
# C.start()
'''