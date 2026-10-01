#**kwargs allows a function to accept any number of keyword arguments, using names and values.

def student(**kwargs):
    print(kwargs)
student(name="Aftab", age=20, course="Python")

