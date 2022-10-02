from base import Vehicle
"""
создайте класс `Car`, наследник `Vehicle`
"""

class Car(Vehicle):
    engine = None

    def set_engine(self, Engine :str):
        self.engine = Engine

