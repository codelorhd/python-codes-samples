# Unlike in other programming languages, methods cannot be explicitly overloaded in Python but can be implicitly overloaded.

# In order to include optional arguments, we assign default values to those arguments rather than creating a duplicate method with the same name. If the user chooses not to assign a value to the optional parameter, a default value will automatically be assigned to the variable.

# Advantages:
# Overloading saves us memory, because creating method is costlier.


class Employee:
    # defining the properties and assigning them to None
    def __init__(self, ID=None, salary=None, department=None) -> None:
        self.ID = ID
        self.salary = salary
        self.department = department

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a = ", a)
        print("b = ", b)
        print("c = ", c)
        print("d = ", d)
        print("e = ", e)

    def tax(self, title=None):
        return self.salary * 0.2

    def salaryPerDay(self):
        return self.salary / 30


# creating an object of the Employee class
Steve = Employee()

# Printing properties of Steve
print("Demo 1")
Steve.demo(1, 2, 3)
print("\n")

print("Demo 2")
Steve.demo(1, 2, 3, 4)
print("\n")

print("Demo 3")
Steve.demo(1, 2, 3, 4, 5)
