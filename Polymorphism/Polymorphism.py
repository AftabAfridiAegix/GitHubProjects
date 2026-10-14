# concept in which the same method, function, or operator can perform different actions depending on the object or data type.

class Animal:
    def sound(sound):
         print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
         print("Dog barks")

d = Dog()
d.sound()