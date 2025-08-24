# Requirement:
# Create a Student class with methods like add_marks(), calculate_grade().
# Use a decorator to log which method is being called.
def log_method(func):
    def wrapper(self,*args,**kwargs):
        print(f"Log method : {func.__name__}")
        return func(self,*args,**kwargs)
    return wrapper

class Student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
    
    @log_method
    def add_marks(self,mark):
        self.marks.append(mark)
        print(f"{mark} has been added successfully..")
    
    @log_method
    def calculate_gpa(self):
        if self.marks:
            avg_mark=sum(self.marks)/len(self.marks)
            return avg_mark
        else:
            print('No anu mark avilable..')
    
if __name__=="__main__":
    student=Student('Amit')
    student.add_marks(50)
    student.add_marks(60)
    student.add_marks(70)

    student.calculate_gpa()