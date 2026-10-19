import csv
import os

FILE = "contacts.csv"

if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])

    print("Contact saved successfully!")

def show_contacts():
    with open(FILE, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            print(" | ".join(row))

while True:
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        print("Program closed.")
        break
    else:
        print("Invalid choice!")