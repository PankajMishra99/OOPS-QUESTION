class Subject:
    def __init__(self,name,mark):
        self.name = name
        self.mark=mark

class Student:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.subjects=[]
    
    def add_subject(self,subject,mark):
        self.subjects.append(Subject(subject,mark))
    
    def calculate_gpa(self):
        if not self.subjects:
            return 'No any subject..'
        total_mark =sum(subject.mark for subject in self.subjects)
        avg_mark = total_mark/len(self.subjects)
        return avg_mark
    
    def get_gpa(self):
        mark=self.calculate_gpa()
        if not mark:
            return None
        
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

if __name__=="__main__":
    system=Student('pankaj',1)

    system.add_subject('math',98)
    system.add_subject('science',95)

    system.calculate_gpa()

    print(system.get_gpa())


