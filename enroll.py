from abc import ABC,abstractmethod
class Person(ABC):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @abstractmethod
    def __str__(self):
        return f"Name {self.name} with age {self.age}"

class Professor(Person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department
    
    def __str__(self):
        return f"Professer name {self.name} with age {self.age} and department {self.department}"

class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id=student_id
    
    def __str__(self):
        return f"Student name {self.name}  age {self.age} with id {self.student_id}"

    def enroll(self,course):
        course.add_student(self)
    
class Course:
        def __init__(self,course_name=None,professor=None,max_seats=None):
            self.course_name=course_name
            self.professor=professor
            self.max_seats=max_seats
            self.students=[]
        
        def add_student(self,student):
            if len(self.students)<self.max_seats:
                self.students.append(student)
                print(f"{student} has been added successfully..")
            else:
                print(f"Course {self.course_name} has been full!")
        
        def show_student(self):
            if self.students:
                for student in self.students:
                    print("Student List: ", student.student_id)
            else:
                print('No student avialable..')
if __name__=="__main__":
    prof = Professor('Mr.A',46,'IT')
    course= Course('Python',prof,50)
    # ---------------------------------------------------
    student1=Student('Amit',29,1)
    student2=Student('Jhon',28,2)


    print(student1.enroll(course))
    print(student2.enroll(course))
    course.show_student()


