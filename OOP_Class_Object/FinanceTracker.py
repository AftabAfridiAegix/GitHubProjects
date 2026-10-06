class FinanceTracker:
    def __init__(self):
       self.transactions = []

    def add_transaction(self, title, amount, category):
        transaction = {
            "title": title,
            "amount": amount,
            "category":category

        }

        self.transactions.append(transaction)

    def show_transactions(self):
        for transaction  in self.transactions:
            print(transaction["title"])
            print(transaction["amount"])
            print(transaction["category"])
            print()

tracker = FinanceTracker()

tracker.add_transaction("salary", 50000, "Income")
tracker.add_transaction("Food", 1500, "Expense")
tracker.add_transaction("Transport", 1000, "Expense")

tracker.show_transactions()




