class Employee:
    def __init__(self,name,id,department,salary):
        self.name=name
        self.id=id
        self.department = department
        self.salary=salary
    
    def update_salary(self,new_salary):
        self.salary=new_salary
    
    def __str__(self):
        return f"{self.name} - {self.id} with  department {self.department}"

class Company:
    def __init__(self):
        self.employees=[]
    
    def add_employee(self,employee):
        self.employees.append(employee)
        print(f"{employee} added successfully..")
    
    def find_employee_id(self,id):
        for emp in self.employees:
            if emp.id==id:
                return emp
            else:
                print (f"{id} does not exist in the list..")
        return None
    
    def show_employee(self):
        if self.employees:
            for emp in self.employees:
                print('Employee list: ',emp)
        else:
            print ('No employee..')
    
    def average_salary(self):
        if self.employees:
            total_salary= 0
            emp_len = 0
            for emp in self.employees:
                total_salary += emp.salary
                emp_len +=1
            avg_salary = total_salary/emp_len
            return avg_salary
        return None

if __name__=="__main__":
    system = Company()
    system.add_employee(Employee('bitu',1,'IT',100000))
    system.add_employee(Employee('Amit',2,'DS',90000))

    system.find_employee_id(1)

    print(system.average_salary())
