class Hospital:

    def __init__(self):
        self.patients = {}

    def add_patient(self):
        patient_id = input("Enter patient ID: ")
        name = input("Enter patient name: ")
        age = int(input("Enter patient age: "))
        disease = input("Enter disease: ")

        self.patients[patient_id] = {
            "name": name,
            "age": age,
            "disease": disease
        }

        print("Patient added successfully.")

    def search_patient(self):
        patient_id = input("Enter patient ID: ")

        if patient_id in self.patients:
            print("Patient found:")
            print(self.patients[patient_id])
        else:
            print("Patient not found.")

    def update_patient(self):
        patient_id = input("Enter patient ID: ")

        if patient_id in self.patients:
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            disease = input("Enter new disease: ")

            self.patients[patient_id] = {
                "name": name,
                "age": age,
                "disease": disease
            }

            print("Patient updated successfully.")
        else:
            print("Patient not found.")

    def delete_patient(self):
        patient_id = input("Enter patient ID: ")

        if patient_id in self.patients:
            del self.patients[patient_id]
            print("Patient deleted successfully.")
        else:
            print("Patient not found.")

    def display_patients(self):
        if not self.patients:
            print("No patient records available.")
        else:
            print("\nPatient Records:")

            for patient_id, details in self.patients.items():
                print("Patient ID:", patient_id)
                print("Name:", details["name"])
                print("Age:", details["age"])
                print("Disease:", details["disease"])
                print("--------------------")


hospital = Hospital()

while True:
    print("\n===== Hospital Patient Management System =====")
    print("1. Add Patient")
    print("2. Search Patient")
    print("3. Update Patient")
    print("4. Delete Patient")
    print("5. Display Patients")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hospital.add_patient()

    elif choice == 2:
        hospital.search_patient()

    elif choice == 3:
        hospital.update_patient()

    elif choice == 4:
        hospital.delete_patient()

    elif choice == 5:
        hospital.display_patients()

    elif choice == 6:
        print("Program ended.")
        break

    else:
        print("Invalid choice.")