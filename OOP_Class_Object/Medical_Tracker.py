class PatientTracker:
     def __init__(self):
         self.patients = []

     def add_patient(self, name, age, disease):
            patient = {
               "name" : name,
                "age" : age,
                "disease" : disease
            
          }

            self.patients.append(patient)

     def show_patients(self):
          for patient in self.patients:
               print(patient["name"])
               print(patient["age"])
               print(patient["disease"])
               print()


tracker = PatientTracker()

tracker.add_patient("Aftab", 23, "fever")
tracker.add_patient("Ali", 34, "Cough")
tracker.add_patient("khuzaima", 45, "head_ache")    

tracker.show_patients()

     

