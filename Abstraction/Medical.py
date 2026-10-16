from abc import ABC, abstractmethod

class Medical(ABC):
    @abstractmethod
    def treatment(self):
        pass
class Patient(Medical):

    def treatment(Medical):
        print("Patient needs a medical checkup")

p = Patient()
p.treatment()