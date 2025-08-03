class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.subjects = {}
    
    def add_subject(self,subject,mark):
        self.subjects[subject]=mark
    
    def get_avgmark(self):
        if not self.subjects:
            return 0
        total_marks = sum(self.subjects.values())
        avg_marks = total_marks/len(self.subjects)
        return avg_marks

    def get_gpa(self):
        mark=self.get_avgmark()

        if mark>90:
            return 'A'
        elif mark>80:
            return 'B'

        elif mark>70:
            return 'C'
        elif mark>60:
            return 'D'
        else:
            return 'E'
    
    def __str__(self):
        return f'{self.name} with {self.id} has total gpa is : {self.get_gpa()}'
        
system = Student('Amit',1)
system.add_subject('Math',98)
system.add_subject('Science',95)
print(system)
