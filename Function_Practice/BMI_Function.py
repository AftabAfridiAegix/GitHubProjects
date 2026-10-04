def calculate_bmi(weight, height):
    bmi = weight /(height ** 2)
    return bmi
def get_category(bmi):
    if bmi < 18.5:
        return "UnderWeight"
    elif bmi < 25:
        return "Healthy weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"



name = input("Enter patient name: ")
weight = float(input("Enter Weight(kg): "))
feet = float(input("Enter Height (feet): "))

height = feet * 0.3048


if weight <= 0 or height <=0:
    print("Weight and Height must be greater than zero.")
else:

    bmi = calculate_bmi(weight, height)
    category = get_category(bmi)
    


    print("\n ---- BMI Report ---")
    print("Patient:", name)
    print(f"Weight: {weight} kg")
    print(f"Height: {feet} ft ")
    print(f"BMI: {bmi:.2f}")
    print("Category:", category)
