class Doctor:
    def consultation_fee(self):
        print("General doctor fee is: Rs. 1000")
class Cardiologist(Doctor):
    def consultant_fee(self):
        print("Cardiologist fee: Rs. 2500")
class Dermatologist(Doctor):
    def consultation_fee(self):
        print("Dermatologist fee: Rs. 2000")

doctors = [
    Doctor(),
    Cardiologist(),
    Dermatologist()
]

for doctor in doctors:
    doctor.consultation_fee()