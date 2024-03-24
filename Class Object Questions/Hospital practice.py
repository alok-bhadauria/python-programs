class Patient:
    
    def __init__(self, patient_id, name, age, contact, gender):
        self.__patient_id = patient_id
        self.__name = name
        self.__age = age
        self.__contact = contact
        self.__gender = gender
        self.__assigned_doctor = None

    def assign_doctor(self, doctor):
        self.__assigned_doctor = doctor

    def view_patient_info(self):
        self.__patient_details = {'Patient ID': self.__patient_id, 'Patient Name': self.__name, 
                             'Patient age': self.__age, 'Patient contact': self.__contact, 
                             'Patient gender': self.__gender, 'Doctor assigned' : self.__assigned_doctor}
        
        print("<<===== Patient Details =====>>".center(28))
        for name, details in self.__patient_details.items():
            print(str(name).rjust(16),' : ',str(details).ljust(16))
        print()

class Doctor:
    
    def __init__(self, doctor_id, name, specialization):
        self.__doctor_id = doctor_id
        self.__name = name
        self.__specialization = specialization
    
    def view_doctor_info(self):
        self.__doctor_details = {'Doctor ID': self.__doctor_id, 'Doctor Name': self.__name, 
                                 'Specialization': self.__specialization}
        
        print("<<===== Doctor Details =====>>".center(28))
        for name, details in self.__doctor_details.items():
            print(str(name).rjust(16),' : ',str(details).ljust(16))
        print()

class MedicalReport:
    
    def __init__(self):
        self.__records = {}

    def AddRecords(self, patient, doctor, diagnosys, medication):
        self.__records[Patient.getDetails()['PatientID']] = {

            'patient' : Patient.getDetails(),
            'doctor' : Doctor.getDoctor_Details(),
            'diagnosys' : diagnosys,
            'medication' : medication
        }

# Main Code

p1 = Patient(1001, "Priyanshu", 18, 9800980098, "Male")
p2 = Patient(1001, "Ayaan", 18, 9700970097, "Male")
p3 = Patient(1001, "DivyaRaj", 18, 9600960096, "Male")

d1 = Doctor(9001, "Manish", "Anatomy")
d2 = Doctor(9002, "Alok", "Neural")

p1.view_patient_info()
p2.view_patient_info()
p3.view_patient_info()
d1.view_doctor_info()
d2.view_doctor_info()