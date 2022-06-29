class Player:
    teamName = "Liverpool"  # class variables

    def __init__(self, name):
        self.name = name  # creating instance variables


p1 = Player("Mark")
p2 = Player("Steve")

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
