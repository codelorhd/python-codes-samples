class Employee:
    def __init__(self, ID, salary) -> None:
        self.ID = ID
        self.__salary = salary  # salary is a private property

    def displaySalary(self):  # displaySalary is a public method
        print("Salary:", self.__salary)

    def __displayID(self):  # displayID is a private method
        print("ID:", self.ID)


Steve = Employee(3789, 2500)
Steve.displaySalary()


# It is not common to have private methods and variables in python, but if you need to do that do it.
# You can access the private variables from a main code by making us of the class Name
Steve = Employee(4789, 4500)
print(Steve._Employee__salary)  # accessing a private property


Steve.__displayID()  # this will generate an error
