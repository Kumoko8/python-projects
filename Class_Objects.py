#Taylor Golden
#Status: Complete

import employee

def main():
    
    #List of all employees
    all_employees = []
    #Ask number of employees
    employee_num = int(input('Enter the number of new employees: '))
    
    #employee_num = number of class instances

    for i in range(employee_num):
    #Prompt user for input data
        print(f'Employee {i + 1}\n')
        employee_name = input('Enter employee name: ')
        employee_ID = int(input('Enter employee ID: '))
        employee_dept = input('Enter department: ')
        employee_title = input('Enter position: ')
        employee_salary = int(input("Enter initial salary: "))
    
    #Create employee_num of instances
        new_employee = employee.Employee(employee_name, employee_ID, employee_title, employee_dept, employee_salary)
    
        salary_change = int(input(f"Salary change for {employee_name}(negative if decreased)"))
    
        if salary_change < 0:
            new_employee.decrease_salary(salary_change)
        else:
            new_employee.increase_salary(salary_change)
            
        all_employees.append(new_employee)
    
    for emp in all_employees:
       print(emp)

    # Salary changes
    
    
    
    
    
#Enter num of employees

#initilizer method


#increase salary method

#decrease salary method

#_str_ method




if __name__ == '__main__':
    main()