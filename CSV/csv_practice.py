# A CSV file is used to store data in a simple tabular format, 
# consisting of rows and columns.
#  Values are usually separated by commas.

import csv

# Write data into CSV file
with open("patients.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Age", "Disease"])
    writer.writerow([1, "Ali", 25, "Flu"])
    writer.writerow([2, "Sara", 30, "Fever"])

print("Data saved successfully!\n")

# Read data from CSV file
with open("patients.csv", "r", newline="") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)