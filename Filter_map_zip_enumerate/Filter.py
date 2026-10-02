# filter() applies that function to every item and keeps only the items that pass the condition.

numbers = [1, 2, 3, 4, 5]

def check(x):
    return x > 3
result = filter(check, numbers)
print(list(result))

def expensive(price):
    return price > 1000
prices = [500, 1500, 800, 2500, 300, 1200]
result = filter(expensive, prices)
print(list(result))

