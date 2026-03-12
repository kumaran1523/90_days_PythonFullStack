# Create a class Employee and child class Manager with extra attribute.

class Employee:
    def __init__(self,e_id,e_name,e_sal):
        self.e_id=e_id
        self.e_name=e_name
        self.e_sal=e_sal
    def emp_details(self):
        print("Employee Details :")
        print(f"Employee ID is : {self.e_id} ")        
        print(f"Employee Name is : {self.e_name} ")        
        print(f"Employee Salary is : {self.e_sal} ")       
class Manager(Employee):
    def __init__(self, e_id, e_name, e_sal,m_name,m_sal):
        super().__init__(e_id, e_name, e_sal)
        self.m_name=m_name
        self.m_sal=m_sal
    def manager_deatils(self):
        self.emp_details()
        print(f"manager Name is : {self.m_name}")
        print(f"manager Salary is : {self.m_sal}")

obj=Manager(123,"Kumar",25000,"Sakthi",50000)
obj.manager_deatils()