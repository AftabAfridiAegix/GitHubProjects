class Patient:
    def __init__(self,name, age):
        self.name = name 
        self.age = age


class BrainAssessment(Patient):
    def assess(self, symptom):
        conditions = {
            "memory loss" : "Memory impairment",
            "tremor" : "Movement related concern",
            "seizure": "Possible neurological concern",
            "headache": "Headache-related concern"

        }


        result = conditions.get(
            symptom.lower(), "Further assessment required"
        )
        print("\n--- Brain Health Report ---")
        print(f"Patient: {self.name} | Age: {self.age}")
        print(f"Reported symptom: {symptom}")
        print(f"Assessment: {result}")
        print("Recommendation: Consult a healthcare professional.")


name = input("Patient name: ")
age = int(input("Patient age: "))
symptom = input("Enter symptom: ")

patient = BrainAssessment(name, age)
patient.assess(symptom)
