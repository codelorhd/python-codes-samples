# By default, all methods and properties are public in nature.


# Example of a private method.
# Access this will give you an error
# Add double underscore to make it private.
class Employee:
    def __init__(self, ID, salary):
        self.ID = ID
        self.__salary = salary  # salary is a private property


Steve = Employee(3789, 2500)
print("ID:", Steve.ID)
print("Salary:", Steve.__salary)  # this will cause an error
