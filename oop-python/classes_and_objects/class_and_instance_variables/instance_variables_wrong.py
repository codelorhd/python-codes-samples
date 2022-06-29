# Wrong use of instance variable
class Player:
    formerTeams = []  # class variables
    teamName = "Liverpool"

    def __init__(self, name):
        self.name = name  # creating instance variables


p1 = Player("Mark")
p2 = Player("Steve")

p1 = Player("Mark")
p1.formerTeams.append("Barcelona")  # wrong use of class variable
# It is wrong because each player is meant to have their unique
# list of former teams they have played with

p2 = Player("Steve")
p2.formerTeams.append(
    "Chelsea"
)  # wrong use of class variable, this is shared for all objects of Player

print("Name:", p1.name)
print("Team Name:", p1.teamName)
print(p1.formerTeams)
print("Name:", p2.name)
print("Team Name:", p2.teamName)
print(p2.formerTeams)
