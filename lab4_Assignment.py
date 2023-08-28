class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employee_data = [
            Employee("161E90", "Raman", 41, 56000),
            Employee("161F91", "Himadri", 38, 67500),
            Employee("161F99", "Jaya", 51, 82100),
            Employee("171E20", "Tejas", 30, 55000),
            Employee("171G30", "Ajay", 45, 44000)
        ]

    def sort_employees(self, parameter):
        if parameter == 1:  # Sort by Age
            sorted_data = sorted(self.employee_data, key=lambda x: x.age)
        elif parameter == 2:  # Sort by Name
            sorted_data = sorted(self.employee_data, key=lambda x: x.name)
        elif parameter == 3:  # Sort by Salary
            sorted_data = sorted(self.employee_data, key=lambda x: x.salary)
        else:
            print("Invalid Option")
            return

        print("\nSorted Employee Data:")
        for employee in sorted_data:
            print(f"Employee ID: {employee.emp_id}, Name: {employee.name}, Age: {employee.age}, Salary (PM): {employee.salary}")

if __name__ == "__main__":
    print("Sorting Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    
    choice = int(input("Enter Your Sorting Choice: "))
    database = EmployeeDatabase()
    database.sort_employees(choice)
