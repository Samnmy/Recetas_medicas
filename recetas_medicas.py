# medical_prescription_manager.py
from datetime import datetime

# Preload the list of prescriptions
def preload_prescriptions():
    # List of prescriptions, each represented as a dictionary
    prescriptions = [
        {"patient": "John Doe", "medicine": "Paracetamol", "dose": "500mg", "frequency": "Every 6 hours", "duration": 5, "date": "2025-05-01"},
        {"patient": "Jane Smith", "medicine": "Ibuprofen", "dose": "200mg", "frequency": "Every 8 hours", "duration": 7, "date": "2025-05-03"},
        {"patient": "Alice Brown", "medicine": "Amoxicillin", "dose": "250mg", "frequency": "Every 12 hours", "duration": 10, "date": "2025-04-25"},
        {"patient": "Bob White", "medicine": "Paracetamol", "dose": "500mg", "frequency": "Every 6 hours", "duration": 3, "date": "2025-04-28"},
        {"patient": "Charlie Black", "medicine": "Ibuprofen", "dose": "200mg", "frequency": "Every 8 hours", "duration": 7, "date": "2025-05-02"}
    ]
    return prescriptions

# Function to register a new prescription
def register_prescription(prescriptions, patient, medicine, dose, frequency, duration, date):
    try:
        # Validate if the duration is a positive number
        duration = int(duration)
        if duration <= 0:
            print("Error: Duration must be a positive number.")
            return
    except ValueError:
        print("Error: Duration must be a valid integer.")
        return
    
    # Validate date format (YYYY-MM-DD)
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Error: Date must be in the format YYYY-MM-DD.")
        return
    
    # Create a new prescription dictionary and append it to the list
    prescription = {"patient": patient, "medicine": medicine, "dose": dose, "frequency": frequency, "duration": duration, "date": date}
    prescriptions.append(prescription)
    print(f"Prescription for {patient} registered successfully.")

# Function to search prescriptions by patient's name
def search_prescription(prescriptions, patient_name):
    results = []
    for prescription in prescriptions:
        if patient_name.lower() in prescription["patient"].lower():
            results.append(prescription)
    return results

# Function to update prescription (dose or duration)
def update_prescription(prescriptions, patient_name, medicine, new_dose=None, new_duration=None):
    for prescription in prescriptions:
        if prescription["patient"].lower() == patient_name.lower() and prescription["medicine"].lower() == medicine.lower():
            if new_dose:
                prescription["dose"] = new_dose
            if new_duration:
                try:
                    new_duration = int(new_duration)
                    if new_duration <= 0:
                        print("Error: Duration must be a positive number.")
                        return
                    prescription["duration"] = new_duration
                except ValueError:
                    print("Error: Duration must be a valid integer.")
                    return
            print(f"Prescription for {patient_name} updated successfully.")
            return
    print(f"Prescription for {patient_name} and {medicine} not found.")

# Function to delete expired prescriptions
def delete_expired_prescriptions(prescriptions):
    today = datetime.today().date()
    to_delete = []
    for prescription in prescriptions:
        # Convert prescription date to datetime object and check if it's expired
        prescription_date = datetime.strptime(prescription["date"], "%Y-%m-%d").date()
        expiration_date = prescription_date.replace(year=prescription_date.year + prescription["duration"])
        
        if expiration_date < today:
            to_delete.append(prescription)
    
    if to_delete:
        confirm = input(f"Are you sure you want to delete {len(to_delete)} expired prescriptions? (yes/no): ")
        if confirm.lower() == 'yes':
            for prescription in to_delete:
                prescriptions.remove(prescription)
            print(f"{len(to_delete)} expired prescriptions deleted successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("No expired prescriptions to delete.")

# Function to generate reports
def generate_reports(prescriptions):
    # Report for the most prescribed medicines
    medicine_count = {}
    for prescription in prescriptions:
        medicine = prescription["medicine"]
        if medicine not in medicine_count:
            medicine_count[medicine] = 0
        medicine_count[medicine] += 1
    
    print("\nMost prescribed medicines:")
    for medicine, count in medicine_count.items():
        print(f"{medicine}: {count} times")
    
    # Report for the average duration of prescriptions
    total_duration = sum([prescription["duration"] for prescription in prescriptions])
    average_duration = total_duration / len(prescriptions) if prescriptions else 0
    print(f"\nAverage prescription duration: {average_duration:.2f} days")

# Main interactive menu function
def menu():
    # Preload the list of prescriptions
    prescriptions = preload_prescriptions()

    while True:
        # Display the menu
        print("\n--- Medical Prescription Management System ---")
        print("1. Register Prescription")
        print("2. Search Prescription")
        print("3. Update Prescription")
        print("4. Delete Expired Prescriptions")
        print("5. Generate Reports")
        print("6. Exit")
        
        # Get user choice
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Prompt for prescription details and register the prescription
            patient = input("Enter patient's name: ")
            medicine = input("Enter medicine name: ")
            dose = input("Enter dose (e.g., 500mg): ")
            frequency = input("Enter frequency (e.g., Every 6 hours): ")
            duration = input("Enter duration (in days): ")
            date = input("Enter prescription date (YYYY-MM-DD): ")
            register_prescription(prescriptions, patient, medicine, dose, frequency, duration, date)

        elif choice == '2':
            # Prompt for patient name and display matching prescriptions
            patient_name = input("Enter patient's name to search: ")
            results = search_prescription(prescriptions, patient_name)
            if results:
                for result in results:
                    print(f"Patient: {result['patient']}, Medicine: {result['medicine']}, Dose: {result['dose']}, Frequency: {result['frequency']}, Duration: {result['duration']} days, Date: {result['date']}")
            else:
                print("No prescriptions found.")

        elif choice == '3':
            # Prompt for patient and medicine to update
            patient_name = input("Enter patient's name to update: ")
            medicine = input("Enter medicine name to update: ")
            new_dose = input("Enter new dose (or leave blank to skip): ")
            new_duration = input("Enter new duration (or leave blank to skip): ")
            update_prescription(prescriptions, patient_name, medicine, new_dose if new_dose else None, new_duration if new_duration else None)

        elif choice == '4':
            # Delete expired prescriptions
            delete_expired_prescriptions(prescriptions)

        elif choice == '5':
            # Generate reports
            generate_reports(prescriptions)

        elif choice == '6':
            # Exit the system
            print("Exiting the medical prescription management system.")
            break

        else:
            # Handle invalid menu choice
            print("Invalid choice. Please try again.")

# Entry point for the program
if __name__ == "__main__":
    menu()
