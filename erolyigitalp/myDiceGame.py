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
        print("'R' for restart the game or")
        print("'Q' for quit")
        restartOrQuit = input(": ")
        if restartOrQuit == "R":
            print("Restarting...")
            gameStart()
        elif restartOrQuit == "Q":
            print("Exiting...")
            quit()
    elif playerBalance <= 0:
        print("You lost your all money. Better luck next time.")
        print("'R' for restart the game or")
        print("'Q' for quit")
        restartOrQuit = input(": ")
        if restartOrQuit == "R":
            print("Restarting...")
            gameStart()
        elif restartOrQuit == "Q":
            print("Exiting...")
            quit()

def oneRound(playerBalance):
    print("You have $" + str(playerBalance) + ".")

    while True:
        print("'Q' for quit or")
        print("Make your bet:")
        print("You can make bet between $1 to $" + str(playerBalance) + ".")
        playerBet = input(": ")

        if playerBet == "Q":
            return "exited"
        try:
            playerBet = int(playerBet)
            if 1 <= playerBet <= playerBalance:
                break
            else:
                print("Your bet must be lower than your balance. Please enter a valid bet.")
        except ValueError:
            print("Invalid input. Please enter a valid bet.")

    dice = Dice()
    roll_sum = 0

    while True:
        dice1 = dice.roll()
        dice2 = dice.roll()
        roll_sum = dice1 + dice2
        print(f"You rolled: {dice1} + {dice2} = {roll_sum}")

        if roll_sum in (7, 11):
            print("You won the bet!")
            return playerBet
        elif roll_sum in (2, 3, 12):
            print("You lost the bet.")
            return -playerBet

if __name__ == "__main__":
    gameStart()