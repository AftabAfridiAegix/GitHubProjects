# The process of combining variables and methods in a class and protecting data from direct access.

class Person:
    def __init__(self, name, age, salary):
        self.name = name          # Public
        self._age = age            # Protected
        self.__salary = salary     # Private

    def show_salary(self):
        print("Salary:", self.__salary)

class Employee(Person):
    def __init__(self, name, age, salary, job):
        super().__init__(name, age, salary)
        self.job = job

    def display(self):
        print("Name:", self.name)
        print("Age:", self._age)
        print("Job:", self.job)
        self.show_salary()

emp = Employee("Aftab", 20, 50000, "Developer")
emp.display()