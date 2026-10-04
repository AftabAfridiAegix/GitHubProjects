
# A function is a reusable block of code designed to perform a specific task. 
# It is defined using the def keyword and executed when it is called.
age = int(input('Enter your age: '))
def check_age(age):
    if age >= 18:
        print("Eligible")
    else:
        print("Not Eligible")
check_age(age)

print("------------------------------------------------------------------------------------")
print("                                                                        ")

def calculate_total(price, quantity):
    return price * quantity
def check_discount(total):
    if total >= 1000:
        return total * 0.10
    return 0


def main():
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    total = calculate_total(price, quantity)
    discount = check_discount(total)
    final_price = total - discount
    print("Total:", total)
    print("Discount:", discount)
    print("Final Price:", final_price)

main()


