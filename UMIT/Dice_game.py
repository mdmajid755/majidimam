

import random

class Die:
    def __init__(self, sides):
        
        self.sides = sides

    def roll(self):
        # in here , the code generate the number between "1 to sides(which max 6)"
        # so if dice come with 4 then te random number will be " 1 * 4 = 4"
        return random.randint(1, self.sides)

def game():
    points = 100  
    while points > 0 and points < 1000:  
        print(f"Points: {points}")  
        while True:  
            try:
                wager = int(input(f"Enter a wager between 1 and {points}: "))  # 7
                if wager < 1 or wager > points:  
                    raise ValueError
                break
            except ValueError:
                print("Invalid wager. Please try again.") 

        die1 = Die(6)  
        die2 = Die(6)  

        while True:  
            roll_sum = die1.roll() + die2.roll()  
            print(f"Dice values: {die1.sides} and {die2.sides} - Sum: {roll_sum}")  # 14
            if roll_sum in [7, 11]:  # "in" function woork as "include" to check these numbers are exist or not
                points += wager  
                print("You won the wager!")  
                break
            elif roll_sum in [2, 3, 12]:  
                points -= wager  
                print("You lost the wager.")  
                break

            input_value = input("Press ENTER to roll again or type 'EXIT' to exit the game: ")  # 21
            if input_value.lower() == 'exit':  
                return
            # in here, the code check if the user
            # input a valid "wager" to continue game
            # if the user only press the "enter" 
            # without any "input" then code will wait for
            # invalid wager
            elif input_value.upper() != '':  
                continue

    if points >= 1000:  
        print("Congratulations! You won the game!") 
    else:  
        print("Sorry, you lost the game.")  

if __name__ == '__main__':  
    game()  
