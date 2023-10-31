import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)
    
if __name__ == "__main__":
    gameStart()

def gameStart():
    playerBalance = 100
