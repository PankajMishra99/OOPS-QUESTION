from abc import ABC, abstractmethod
class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id = emp_id
        self.__salary=None
        self.set_salary(salary)
    
    def __str__(self):
        return f"Employee name {self.name} and {self.emp_id} with salary {self.__salary}"
    
    def getter(self):
        return self.__salary
    
    def setter(self,new_salary):
        self.__salary =new_salary
    
    def set_salary(self,value):
        if value<0:
            raise ValueError ('Salary can not be negative..')
        self.__salary=value

class Developer (Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id,salary)
    
    def work(self):
        return "Developer work.."

class Manager(Employee):
    def __init__(self,name,id,salary):
        super().__init__(name,id,salary)
        self.devlopers=[]
    
    def add_devloper(self,developer):
        if len(developer.name)>0:
            self.devlopers.append(developer)
            print(f"{developer.__class__.__name__} has been added successfully..")
        else:
            raise NameError('Please enter the correct name..')
    
    def work(self):
        return f'Manager {self.name} is managing {len(self.devlopers)} devloper'
    

class Department(ABC):
    @staticmethod
    def department_info(self):
        pass
if __name__=="__main__":
    devloper1 = Developer('Mr.a',1,50000)
    devloper2 = Developer('Mr.b',2,70000)

    manager  =Manager('mr.m',11,200000)

    manager.add_devloper(devloper1)
    manager.add_devloper(devloper2)

    print(manager.work())



    

