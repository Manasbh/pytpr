class Employee:
    def _init_(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

def sort_employees(employees, sort_parameter):
    if sort_parameter == 1:
        return sorted(employees, key=lambda emp: emp.age)
    elif sort_parameter == 2:
        return sorted(employees, key=lambda emp: emp.name)
    elif sort_parameter == 3:
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        return employees

#----

#---

def print_employee_table(employees):
    print("Employee ID | Name     | Age | Salary (PM)")
    print("-" * 40)
    for emp in employees:
        print(f"{emp.emp_id}  | {emp.name} | {emp.age}  | {emp.salary}")
    
employee1 = Employee("161E90", "Raman", 41, 56000)
employee2 = Employee("161F91", "Himadri", 38, 67500)
employee3 = Employee("161F99", "Jaya", 51, 82100)
employee4 = Employee("171E20", "Tejas", 30, 55000)
employee5 = Employee("171G30", "Ajay", 45, 44000)

employees = [employee1, employee2, employee3, employee4, employee5]

print("Choose sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")
sort_parameter = int(input("Enter your choice: "))

sorted_employees = sort_employees(employees, sort_parameter)

print_employee_table(sorted_employees)