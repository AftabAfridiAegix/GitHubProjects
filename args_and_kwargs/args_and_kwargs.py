def student(name, *marks, **details):
    print("Name:", name)
    for key, value in details.items():
        print(key, ":", value)
    print("Marks:", marks)
    print("Total:", sum(marks))
    print("Average:", sum(marks) / len(marks))

student("Aftab", 85, 90, 75,
        age=20, department="CS")