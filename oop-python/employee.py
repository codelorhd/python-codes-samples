class Employee:
    def __init__(self, ID=None, salary=None, department=None):
        self.ID = ID
        self.salary = salary
        self.department = department


Steve = Employee(3790, 2500, "Human Resources")

# * Creating a new attribute for Steve
# Steve.title = "Manager"

# Printing the properties of Steve
print("ID = ", Steve.ID)
print("Salary ", Steve.salary)
print("Department: ", Steve.department)


Mark = Employee()
print("ID = ", Mark.ID)
print("Salary ", Mark.salary)
print("Department: ", Mark.department)
