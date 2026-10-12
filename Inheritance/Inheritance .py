# Inheritance is an OOP concept in which one class receives the 
# properties (variables) and methods (functions) of another class.

class Parent:
    def __init__(self, name):
        self.name = name 

    def eat(self):
        print(self.name, "is eating")

class Child(Parent):
    def study(self):
        print(self.name, "is studying")

c1 = Child("Ali")

c1.eat()
c1.study()
