from abc import ABC
from exceptions import LowFuelError, NotEnoughFuel, CargoOverload
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
        #if self.weight == weight and self.fuel_consumption == fuel_consumption and self.fuel == fuel:
        #   print('They are the same')

    def start(self):
        if self.started == False:   #Если
            if self.fuel > 0:
                self.started = True
            elif self.fuel <= 0:
                raise LowFuelError()
        else:
            pass

    def move(self, way):
        if self.fuel <= 0:
            raise Exception('NotEnoughFuel')
        elif self.fuel > 0:
            PossibleWay = (self.fuel // self.fuel_consumption) * 100
            if PossibleWay >= way:
                self.fuel = ((PossibleWay - way) / 100) * self.fuel_consumption
                #Стоит ли упрощать данный пример с помощью переменной? Без неё получается очень длинный пример
            else:
                Exception('NotEnoughFuel')

C = Vehicle(1230302013, 342,  400)