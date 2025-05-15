#Class Employee
class Employee:
    def __init__(self, name, id, title, dept, salary):
        self.__name = name
        self.__id = id
        self.__title = title
        self.__dept = dept
        self.__salary = salary
    #Set methods
    def set_name(self, name):
        self.__name = name
    
    def set_ID(self, id):
        self.__id = id
        
        
    def set_dept(self, dept):
        self.__dept = dept
        
        return
    def set_title(self, title):
        self.__title = title
        
        return
    def set_salary(self, salary):
        self.__salary = salary
        
        return
    def increase_salary(self, increase):
        self.__salary += increase
        
    def decrease_salary(self, decrease):
        if self.__salary >= decrease:
            self.__salary += decrease
        else:
            print('Salary cannot be negative')
            
    #Get methods
    def get_name(self):
        return self.__name
    def get_ID(self):
        return self.__id
    def get_title(self):
        return self.__title
    def get_dept(self):
        return self.__dept
    def get_salary(self):
        return self.__salary
    
    def add_employee(self, employee):
        if len(self.employees) >  0:
            self.employees.append(employee)
        return True
    
    def __str__(self):
        return f"Name: {self.__name}\n ID Number: {self.__id}\n Department: {self.__dept}\n Position: {self.__title}\n New Salary: ${self.__salary}"
    