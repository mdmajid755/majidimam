import random

class Die:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

def main():
    player_points = 0

    while True:
        print(f"Your total points: {player_points}")
        wager = input("Enter your wager (1-100), or type 'EXIT' to quit: ")
        
        if wager.upper() == 'EXIT':
            print("Thanks for playing. Goodbye!")
            break

        try:
            wager = int(wager)
            if wager < 1 or wager > 100:
                print("Invalid wager. Please enter a valid wager.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid wager.")
            continue

        roll = input("Roll the dice? (yes/no): ")
        if roll.lower() == "yes" or roll.lower() == "y":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
        
            roll_sum = die1 + die2
            print(f"Dice roll: {die1} + {die2} = {roll_sum}")

            if roll_sum == 7 or roll_sum == 11:
                player_points += wager
                print(f"You won {wager} points!")
            elif roll_sum == 2 or roll_sum == 3 or roll_sum == 12:
                player_points -= wager
                print(f"You lost {wager} points.")
            
            if player_points <= 0:
                print("You lost the game. Better luck next time!")
            elif player_points >= 1000:
                print("Congratulations! You won the game!")
        
        play_again = input("Would you like to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    main()

    
# first, define min and max dice points at once

# then, we should have while loop 

# roll the dices

# print dice1 score and dice2 score each time  

#calculate dice total

#print dice total for the player

#if dice is rolled between 7-11

   #player wins bc points added

#if dice is rolled between 2-3-12

    #player loses bc points subtracted

#loop continue untill winner points hit 1000 or 0 lose the game 

#exit the game and start it again.

