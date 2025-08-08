class Course:
    def __init__(self,course_id,name,instructor):
        self.course_id=  course_id
        self.name=name
        self.instructor=instructor
    
    def __str__(self):
        return f"{self.name} with id {self.course_id}"

class Student:
    def __init__(self):
        self.courses=[]
    
    def add_course(self,course):
        self.courses.append(course)
    
    def student_enrolled_courses(self):
        if not self.courses:
            print('No Courses avilable..')
        for course in self.courses:
            print ('Course Name :',course)


if __name__=="__main__":
    student = Student()
    student.add_course(Course(1,'Python','Mr. A'))
    student.add_course(Course(2,'Data Science','Mr. B'))
    student.student_enrolled_courses()