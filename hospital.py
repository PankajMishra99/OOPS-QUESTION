from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @abstractmethod
    def display_info(self):
        return f"Person name {self.name} with age {self.age}"

class Doctor(Person):
    def __init__(self,name,age,specialization):
        super().__init__(name,age)
        self.spec=specialization
    
    def display_info(self):
        return f"Doctor name {self.name} and age {self.age} with specilazation {self.spec}"

class Patients(Person):
    def __init__(self,name,age,disease):
        super().__init__(name,age)
        self.disease=disease
    
    def display_info(self):
        return f"Patient name {self.name} with age {self.age} and {self.disease}"

class Appointement:
    def __init__(self,doctor,patient,date):
        self.doctor=doctor
        self.patient=patient
        self.date=date
    def display_info(self):
        print("Appoitment at date :",self.date)
        print(self.doctor.display_info())
        print(self.patient.display_info())

class Hospital:
    def __init__(self):
        self.appoitements=[]
    
    def book_appoitment(self,doctor,patient,date):
        self.appoitements.append(Appointement(doctor,patient,date))
        print('Appoitment booked successfully..')
    
    def view_appoitments(self):
        if self.appoitements:
            for appt in self.appoitements:
                print("Appointment : ",appt.display_info())
        return None


if __name__=="__main__":
    hospital = Hospital()
    hospital.book_appoitment(Doctor('Mr.A',40,'Fever'),Patients('Mr.B',46,'Fever'),'2025-08-10')
    hospital.book_appoitment(Doctor('Mr.C',40,'Fever'),Patients('Mr.D',46,'Fever'),'2025-08-10')

    hospital.view_appoitments()