class BankAccount:
    def __init__(self, name, amount):
        self.name = name
        self.balance = amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Balance insufficient")
    def display(self):
        print("Name", self.name)
        print("Balance", self.balance)

account1 = BankAccount("Aftab", 1000)
account1.display()
account1.deposit(5000)
account1.display()
account1.withdraw(3000)
account1.display()



       
