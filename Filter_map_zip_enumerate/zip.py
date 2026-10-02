# zip() combines items from two or more lists based on their positions. It pairs the first item of each list, then the second, and so on.

names = ["Ali", "Ahmed", "Sara"]
marks = [85, 90, 78]
result = zip(names, marks)

print(list(result))


def show_expense(date, amount):
    print(f"{date} : Rs. {amount}")
dates = ["Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday"]
expenses = [500, 300, 750, 200, 450]

total = 0

print("===== EXPENSE REPORT =====")
for date, amount in zip(dates, expenses):
    show_expense(date, amount)
    total += amount
print("--------------------------")
print("Total spending: Rs.", total)
print("Average spending: Rs.", total / len(expenses))

if total > 2000:
    print("Warning: High spending!")
else:
    print("Spending is within budget.")