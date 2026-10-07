class Trapezoid:
    def __init__(self, name, a, base, height):
        self.name = name
        self.a = a
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.a + self.base) * self.height

tra = Trapezoid("Trapezoid A", 5, 7 , 4)
print(f"{tra.name} Area: {tra.calculate_area()}")



    
    