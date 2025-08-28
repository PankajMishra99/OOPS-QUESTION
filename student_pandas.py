import pandas as pd
class Student:
    def __init__(self,id,name,age,marks):
        self.id=id
        self.name=name
        self.age=age
        self.marks=marks

class Student_Manager:
    def __init__(self):
        self.data=pd.DataFrame(columns=['id','name','age','marks'])
    
    def add_student(self,student:Student):
        new_row={
            'id':student.id,
            'name':student.name,
            'age':student.age,
            'marks':student.marks
        }
        self.data = pd.concat([self.data,pd.DataFrame([new_row])],ignore_index=True)
    
    def studentlist(self):
        if self.data.empty:
            print("No information avialble in the student list..")
        print(self.data)
    
    def average_marks(self):
        if self.data.empty:
            return "No student avilable in the list"
        return self.data['marks'].mean()

    def pandas_filter(self):
        if self.data.empty:
            return 'No student avilable in the list..'
        return (self.data[self.data['marks']>=60])

if __name__=="__main__":
    student_manager=Student_Manager()
    student_manager.add_student(Student(1,'Amit',29,52))
    student_manager.add_student(Student(2,'Neha',28,92))
    student_manager.add_student(Student(3,'Rahul',29,97))
    student_manager.add_student(Student(4,'bitu',29,98))

    student_manager.studentlist()
    print(student_manager.average_marks())
    print(student_manager.pandas_filter())
        