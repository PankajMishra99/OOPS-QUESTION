class Employee:
    def __init__(self,name,emp_id,salary):
        self.name=name
        self.emp_id=emp_id
        self._salary=salary # protected variable
    
    def get_details(self):
        return f"Name {self.name} - Id {self.emp_id} with {self._salary}"
    
    def getter(self):
        return self.__salary

    def setter(self,new_salary:float):
        if self._salary>0:
            self._salary=new_salary
        else:
            raise ValueError('Salary must be postive')

class Manager(Employee):
    def __init__(self,name,emp_id,salary,team_size=5):
        super().__init__(name,emp_id,salary)
        self.team_size=team_size
    
    def get_details(self):
        return f"Manager name {self.name} with id {self.emp_id}, team size {self.team_size} and manager salary - {self._salary}"

    def setter(self, new_salary):
        return super().setter(new_salary)
    
    def getter(self):
        return super().getter()

class Developer(Employee):
    def __init__(self,name,emp_id,salary,prm_lg='pyhton'):
        super().__init__(name,emp_id,salary)
        self.prm_lg = prm_lg
    
    
    def get_details(self):
        return super().get_details()
    
    def setter(self, new_salary):
        return super().setter(new_salary)
    
    def getter(self):
        return super().getter()

if __name__=="__main__":
    e1=Manager('M1',101,70000)
    e2=Developer('D1',201,60000)

    print(e1.get_details())
    print(e2.get_details())




