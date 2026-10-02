# map() is used to apply a function to every item in a list and return the changed values

def increase_price(price):
    return round(price * 1.10, 2)
prices = [100, 200, 300, 500]
new_prices = map(increase_price, prices)
print(list(new_prices))


# Function to square a single number
def square(number):
    return number * number
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)

