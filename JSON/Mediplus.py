import json

patient = [
       {"name": "Ali", "age": 25, "disease": "Flu"},
    {"name": "Sara", "age": 30, "disease": "Fever"},
    {"name": "Ahmed", "age": 22, "disease": "Cold"}
   
]

with open("patient.json", "w") as file:
    json.dump(patient, file, indent= 4)

with open("patient.json", "r") as file:
    data = json.load(file)

for patient in data:
      print(
        "Patient Name:", patient["name"],
        "Patient Age:", patient["age"],
        "Disease:", patient["disease"]
    )
