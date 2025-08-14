import datetime
class Student:
    def __init__(self,roll_number,name):
        self.roll_number=roll_number
        self.name=name
        self.attendance={}
    
    def mark_attendance(self,date,status):
        self.attendance[date]=status
    
    def get_attendance_percentage(self):
        total_len=len(self.attendance)
        if total_len ==0:
            return 0
        attend_mark= sum(1 for status in self.attendance.values() if status=='P')
        attend_perc = attend_mark/total_len * 100
        return attend_perc
    
class Attendance_Manager:
    def __init__(self):
        self.students=[]
    
    def add_studnets(self,name,roll_number):
        if any(s.roll_number==roll_number   for s in self.students):
            print (f"{roll_number} has been already exist..")
        student=self.students.append(Student(roll_number,name))
        print(f"Student name {name} with {roll_number} has been updated sucessfully..")
        return student
    
    def mark_attendance_for_date(self,date):
        for student in self.students:
            status= input(f"Mark attendance {student.name}.: ").upper()
            if status in ('P','A'):
                student.mark_attendance(date,status)
            
        print('Attendance marked successfully.')
    
    def view_student(self):
        if self.students:
            for student in self.students:
                print(f'Student Views : {student.name}-{student.roll_number}','/n')
        else:
            print('No student avilable in the list')
    
    def view_attendance_for_specific_student(self,name):
        if self.students:
            for student in self.students:
                if student.name==name:
                    return student.attendance
        else:
            print('No student to view..')

if __name__=='__main__':
    manager=Attendance_Manager()
    
    while True:
        choice=int(input("Please enter the input: "))

        if choice ==1:
            roll_no = int(input("Please enter the roll_no: "))
            name=input("Please enter the student' name: ")
            manager.add_studnets(name,roll_no)
        
        elif choice ==2:
            date = input("Enter the date (YYYY-MM-DD)")
            if not date:
                date=datetime.today().strftime('%y-%m-%d')
            manager.mark_attendance_for_date(date)
        
        elif choice==3:
            manager.view_student()
        
        elif choice==4:
            name=input("Please enter the student's name: ")
            manager.view_attendance_for_specific_student(name)
        else:
            break
    
    