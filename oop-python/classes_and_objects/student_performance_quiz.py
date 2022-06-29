class Student:
    total_marks = 100

    def __init__(self, name: int, phy: int, chem: int, bio: int) -> None:
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return sum([self.phy, self.chem, self.bio])

    def percentage(self):
        return int((self.totalObtained() / (self.total_marks * 3)) * 100)


markStudent = Student("Mark", 80, 90, 40)
print((markStudent.percentage()))
