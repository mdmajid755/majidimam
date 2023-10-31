import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def gameStart():
    playerBalance = 100
    while playerBalance > 0 and playerBalance < 1000:
        status = oneRound(playerBalance)
        if status == "exited":
            break
        playerBalance += status
    if status == "exited":
        print("Exiting...")
    elif playerBalance >= 1000:
        print("Congratulation! You won max win!")
    elif playerBalance <= 0:
        print("You lost your all money. Better luck next time.")

def oneRound(playerBalance):
    print("You have $" + playerBalance + ".")

if __name__ == "__main__":
    gameStart()