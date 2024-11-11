
PATIENT_FILE = 'patients.txt'
DISCHARGED_FILE = 'discharged.txt'

def add_patient():
    try:
        with open(PATIENT_FILE, 'a') as file:
            pid = input("Enter Patient ID: ")
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            gender = input("Enter Patient Gender: ")
            diagnosis = input("Enter Diagnosis: ")
            room_no = input("Enter Room Number: ")

            record = f"{pid},{name},{age},{gender},{diagnosis},{room_no}\n"
            file.write(record)
            print(f"Patient {name} added successfully!\n")
    except Exception as e:
        print("Error while adding patient:", e)

def view_patients():
    try:
        with open(PATIENT_FILE, 'r') as file:
            records = file.readlines()
            if len(records) == 0:
                print("No patient records found.\n")
            else:
                print("Patient Records:\n")
                for record in records:
                    fields = record.strip().split(',')
                    print(f"ID: {fields[0]}, Name: {fields[1]}, Age: {fields[2]}, Gender: {fields[3]}, Diagnosis: {fields[4]}, Room: {fields[5]}")
                print()
    except FileNotFoundError:
        print("No patient records found.\n")
    except Exception as e:
        print("Error while viewing patients:", e)

def search_patient():
    pid = input("Enter Patient ID to search: ")
    found = False
    try:
        with open(PATIENT_FILE, 'r') as file:
            records = file.readlines()
            for record in records:
                fields = record.strip().split(',')
                if fields[0] == pid:
                    print(f"Patient Found - ID: {fields[0]}, Name: {fields[1]}, Age: {fields[2]}, Gender: {fields[3]}, Diagnosis: {fields[4]}, Room: {fields[5]}")
                    found = True
                    break
            if not found:
                print("Patient not found.\n")
    except FileNotFoundError:
        print("No patient records found.\n")
    except Exception as e:
        print("Error while searching for patient:", e)

def delete_patient():
    pid = input("Enter Patient ID to delete: ")
    updated_records = []
    found = False
    try:
        with open(PATIENT_FILE, 'r') as file:
            records = file.readlines()
            for record in records:
                fields = record.strip().split(',')
                if fields[0] != pid:
                    updated_records.append(record)
                else:
                    found = True
        if found:
            with open(PATIENT_FILE, 'w') as file:
                file.writelines(updated_records)
            print(f"Patient with ID {pid} deleted successfully.\n")
        else:
            print("Patient ID not found.\n")
    except FileNotFoundError:
        print("No patient records found.\n")
    except Exception as e:
        print("Error while deleting patient:", e)

def update_patient():
    pid = input("Enter Patient ID to update: ")
    updated_records = []
    found = False
    try:
        with open(PATIENT_FILE, 'r') as file:
            records = file.readlines()
            for record in records:
                fields = record.strip().split(',')
                if fields[0] == pid:
                    found = True
                    print("Enter new details for the patient (Leave blank to keep current value):")
                    new_name = input(f"Name [{fields[1]}]: ") or fields[1]
                    new_age = input(f"Age [{fields[2]}]: ") or fields[2]
                    new_gender = input(f"Gender [{fields[3]}]: ") or fields[3]
                    new_diagnosis = input(f"Diagnosis [{fields[4]}]: ") or fields[4]
                    new_room = input(f"Room No. [{fields[5]}]: ") or fields[5]
                    updated_record = f"{pid},{new_name},{new_age},{new_gender},{new_diagnosis},{new_room}\n"
                    updated_records.append(updated_record)
                else:
                    updated_records.append(record)
        if found:
            with open(PATIENT_FILE, 'w') as file:
                file.writelines(updated_records)
            print(f"Patient with ID {pid} updated successfully.\n")
        else:
            print("Patient ID not found.\n")
    except FileNotFoundError:
        print("No patient records found.\n")
    except Exception as e:
        print("Error while updating patient:", e)

def generate_bill():
    pid = input("Enter Patient ID to generate bill: ")
    found = False
    try:
        with open(PATIENT_FILE, 'r') as file:
            records = file.readlines()
            for record in records:
                fields = record.strip().split(',')
                if fields[0] == pid:
                    found = True
                    print("Bill Details for Patient:")
                    print(f"Patient ID: {fields[0]}, Patient Name: {fields[1]}, Room No: {fields[5]}")
                    days = int(input("Enter number of days stayed: "))
                    cost_per_day = 1000
                    total_cost = days * cost_per_day
                    print(f"Total Cost: ${total_cost}")
                    break
            if not found:
                print("Patient not found.\n")
    except FileNotFoundError:
        print("No patient records found.\n")
    except Exception as e:
        print("Error while generating bill:", e)

def discharge_patient():
    pid = input("Enter Patient ID to discharge: ")
    updated_records = []
    found = False
    try:
        with open(PATIENT_FILE, 'r') as file:
            records = file.readlines()
            for record in records:
                fields = record.strip().split(',')
                if fields[0] != pid:
                    updated_records.append(record)
                else:
                    found = True
                    with open(DISCHARGED_FILE, 'a') as discharge_file:
                        discharge_file.write(record)
                    print(f"Patient with ID {pid} has been discharged.\n")
        if found:
            with open(PATIENT_FILE, 'w') as file:
                file.writelines(updated_records)
        else:
            print("Patient ID not found.\n")
    except FileNotFoundError:
        print("No patient records found.\n")
    except Exception as e:
        print("Error while discharging patient:", e)

def view_discharged_patients():
    try:
        with open(DISCHARGED_FILE, 'r') as file:
            records = file.readlines()
            if len(records) == 0:
                print("No discharged patient records found.\n")
            else:
                print("Discharged Patient Records:\n")
                for record in records:
                    fields = record.strip().split(',')
                    print(f"ID: {fields[0]}, Name: {fields[1]}, Age: {fields[2]}, Gender: {fields[3]}, Diagnosis: {fields[4]}, Room: {fields[5]}")
                print()
    except FileNotFoundError:
        print("No discharged patient records found.\n")
    except Exception as e:
        print("Error while viewing discharged patients:", e)

def count_patients():
    try:
        with open(PATIENT_FILE, 'r') as file:
            records = file.readlines()
            print(f"Total number of patients: {len(records)}")
    except FileNotFoundError:
        print("No patient records found.\n")
    except Exception as e:
        print("Error while counting patients:", e)

def main():
    print("========== Hospital Management System ==========")
    print("              Created by Devesh Dixit           ")
    while True:
        print("\n============= Main Menu =============")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Update Patient")
        print("6. Generate Bill")
        print("7. Discharge Patient")
        print("8. View Discharged Patients")
        print("9. Count Patients")
        print("10. Exit")
        print("=====================================")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            search_patient()
        elif choice == '4':
            delete_patient()
        elif choice == '5':
            update_patient()
        elif choice == '6':
            generate_bill()
        elif choice == '7':
            discharge_patient()
        elif choice == '8':
            view_discharged_patients()
        elif choice == '9':
            count_patients()
        elif choice == '10':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
