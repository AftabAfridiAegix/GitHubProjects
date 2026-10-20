# temperature converter

Temp = float(input("Enter Temperature: "))
choice = input("Enter C for Celsius or F for Fahrenheit: ")

if choice == "C":
    fahrenheit = (Temp * 9/5) + 32
    print("Fahrenheit =", fahrenheit)

elif choice == "F":
    celsius = (Temp - 32) * 5/9
    print("Celsius =", celsius)

else:
    print("Invalid Choice")