# Abstraction: Hiding implementation details and showing only the essential features of an object.

from abc import ABC, abstractmethod
class Car(ABC):
    @abstractmethod
    def start(self):
        pass 

class Toyota(Car):
    def start(self):
        print("Car Started")

car = Toyota()
car.start()