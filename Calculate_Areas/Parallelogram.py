
class Parallelogram:
       def __init__(self, name, base, height):
              self.name = name
              self.base = base
              self.height = height

       def calculate_area(self):
              return self.base * self.height
shape1 = Parallelogram("Parallelogram A", 5, 7)

print(f"{shape1.name} Area: {shape1.calculate_area()}")