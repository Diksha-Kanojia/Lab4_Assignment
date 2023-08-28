# Employee data
employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000}
]

def sort_employees(parameter):
    if parameter==1:  # Sort by Age
        sorted_data=sorted(employee_data, key=lambda x: x["Age"])
    elif parameter==2:  # Sort by Name
        sorted_data=sorted(employee_data, key=lambda x: x["Name"])
    elif parameter==3:  # Sort by Salary
        sorted_data=sorted(employee_data, key=lambda x: x["Salary (PM)"])
    else:
        print("Invalid Option")
        return

    print("\nSorted Employee Data: ")
    for employee in sorted_data:
        print(employee)

if __name__ == "__main__":
    print("Sorting Options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    
    choice = int(input("Enter Your Sorting Choice: "))
    sort_employees(choice)
    