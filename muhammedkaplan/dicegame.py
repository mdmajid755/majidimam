import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def game():
    player_points = 100  # Starting points
    while player_points > 0 and player_points < 1000:
        print(f'Player Points: {player_points}')

        # Get player's wager
        while True:
            wager = input("Enter your wager (1 to your current points, or 'exit' to quit): ")
            if wager.lower() == 'exit':
                print("Exiting the game.")
                return
            try:
                wager = int(wager)
                if 1 <= wager <= player_points:
                    break
                else:
                    print("Invalid wager. Please enter a valid wager.")
            except ValueError:
                print("Invalid input. Please enter a valid number or 'exit'.")

        # Roll the dice
        die1 = Die(6).roll()
        die2 = Die(6).roll()
        total = die1 + die2
        print(f"Dice Roll: {die1} + {die2} = {total}")

        # Check for win/loss
        if total in (7, 11):
            print("You win!")
            player_points += wager
        elif total in (2, 3, 12):
            print("You lose!")
            player_points -= wager

    if player_points >= 1000:
        print("Congratulations! You've won the game.")
    else:
        print("Sorry, you've lost the game.")

if __name__ == '__main__':
    game()

