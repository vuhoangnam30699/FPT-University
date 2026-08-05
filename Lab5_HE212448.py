class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.id = emp_id
        self.name = name
        self.age = age
        self.salary = salary
        
    def __str__(self):
        return f"{self.id} {self.name} {self.age} {self.salary}"
    
class EmployeeManager:

    def __init__(self):
        self.employees = []

    # 1 Add employee, check employee Id.
    def add_employee(self):
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = int(input("Enter Salary: "))
        
        for emp in self.employees:
            if emp.id == emp_id:
                print(f"id {emp_id} already existed")
                return
                
        new_employee = Employee(emp_id, name, age, salary)
        self.employees.append(new_employee)


    # 2 Display employees
    def f2(self):
        for i, emp in enumerate(self.employees, 1):
            print(f"{i} {emp}")

    # 3 Find employee by name
    def f3(self, emp_name):
        return [emp for emp in self.employees if emp_name.lower() in emp.name.lower()]

    # 4 Search employee by ID
    def f4(self,emp_id):        
        for emp in self.employees:
            if emp.id == emp_id:
                return emp
        return None

    # 5 Update salary
    def f5(self, emp_id, salary):
        emp = self.f4(emp_id)
        if emp:
            emp.salary = salary
            print("Salary updated")

    # 6 Delete employee
    def f6(self, emp_id):
        emp = self.f4(emp_id)
        if emp:
            self.employees.remove(emp)

    # 7 Sort by salary
    def f7(self):
        self.employees.sort(key=lambda emp: emp.salary, reverse=True)

    # 8 Find salary greater than X
    def f8(self, x):
        return [emp for emp in self.employees if emp.salary > x]

    # 9 Count employees
    def f9(self):
        return len(self.employees)

    # 10 Average salary
    def f10(self):
        if not self.employees:
            return 0.0
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary / len(self.employees)
    
def menu():

    manager = EmployeeManager()
    manager.employees.append(Employee('FPT1','Nguyen Van Thang',35,5000))
    manager.employees.append(Employee('FPT2','Nguyen Ngoc Tuan',30,6000))
    manager.employees.append(Employee('FPT3','Vu Van Huy',39,4000))
    manager.employees.append(Employee('FPT4','Do Thi Loan',34,7000))
    manager.employees.append(Employee('FPT5','Pham Ngoc Tho',35,15000))
    
    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add employee")
    print("2. Display employees")
    print("3. Search employee by ID")
    print("4. Search employee by Name")
    print("5. Update salary")
    print("6. Delete employee")
    print("7. Sort employees by salary")
    print("8. Find employees with salary greater than X")
    print("9. Count employees")
    print("10. Average salary")
    print("0. Exit")
    while True:        
        choice = input("Enter choice: ")
        if choice == "1":
            manager.add_employee()
        elif choice == "2":
            manager.f2()
        elif choice == "3":
            #find name
            emp_name=input('Enter name to search:')
            list=manager.f3(emp_name)
            if len(list)==0:
                print('Not found')
            else :
                for i in list:
                    print(i)

        elif choice == "4":
            emp_id=input('Enter Id to search')
            emp=manager.f4(emp_id)
            if emp is None :
                print('Not found')
            else:
                print(emp)          
        elif choice == "5":
            emp_id=input('Eneter id:')
            salary=int(input('Enter salary:'))
            manager.f5(emp_id,salary)            

        elif choice == "6":
            emp_id=input('Eneter id to delete:')
            manager.f6(emp_id)
            print('Employees after delete')
            manager.f2()

        elif choice == "7":
            manager.f7()
            print('Employees after sort')
            manager.f2()           
        elif choice == "8":
            salary=int(input('Enter x:'))
            list=manager.f8(salary)
            if len(list)==0:
                print('Not found')
            else:
                print(f'List of Employees with salary > {salary}')
                for i in list:
                    print(i)
        elif choice == "9":
            print(f'There is/are {manager.f9()} in the list')
        elif choice=="10":            
            print(f'Average of salary is {manager.f10()}')
        elif choice == "0":
            print("Program ended")
            break
        
        else:
            print("Invalid choice")
menu()
