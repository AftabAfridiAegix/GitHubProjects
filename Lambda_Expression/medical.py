patients = ["Ali", "Ahmed", "Sara", "Usman"]
temps = [38, 36, 39, 37]

check = lambda t: t >= 3
for name, temp in zip(patients, temps):
    if check(temp):
        print(name, "Fever")
    else:
        print(name, "Normal")