def check_temperature(temp):
    if temp < 35:
        return "low temperature"
    elif temp < 38:
        return "Normal range"
    elif temp < 39:
        return "Fever"
    else:
        return "High Temperature"



temperature = float(input("Enter temperature in Celsius: "))
result = check_temperature(temperature)
print("Temmperature: ", temperature, "Celsius")
print("Result:", result)