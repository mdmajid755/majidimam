import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

playerBalance = 100

while playerBalance > 0 and playerBalance < 1000:

    print("You have $" + str(playerBalance) + ".")
    print("'Q' for quit or")
    print("Make your bet:")
    print("You can make bet between $1 to $" + str(playerBalance) + ".")
    playerInput = input(": ")
    try:
        val = int(playerInput)
    except ValueError:
        print("That's not an int!")