import random

class Die:
    def __init__(self, num_sides):
        self.num_sides = num_sides

    def roll(self):
        return random.randint(1, self.num_sides)

def play_game():
    
    player_points = input("Enter Player Initial Points Between 1-1000. (e.g., 100): ")

    
    player_points = int(player_points)

    
    if player_points <= 0:
        print("Invalid initial points. Starting with 100 points.")
        player_points = 100

    while player_points > 0 and player_points < 1000:
        
        print("Player's points:", player_points)

        
        wager = input("Enter a wager (1 to " + str(player_points) + ") or type 'exit' to quit: ")

        
        if wager.lower() == 'exit':
            break

        
        wager = int(wager)

        
        if wager < 1 or wager > player_points:
            print("Invalid wager. Please enter a valid wager.")
            continue

        
        die1 = Die(6)
        die2 = Die(6)
        roll1 = die1.roll()
        roll2 = die2.roll()

        
        print("Dice roll: " + str(roll1) + " and " + str(roll2))

        
        dice_sum = roll1 + roll2

        
        if dice_sum == 7 or dice_sum == 11:
            print("You win the wager!")
            player_points += wager
        elif dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
            print("You lose the wager.")
            player_points -= wager

    
    if player_points >= 1000:
        print("Congratulations! You've won the game!")
    elif player_points <= 0:
        print("Sorry, you've lost the game.")

while True:
    play_game()
    choice = input("Do you want to restart the game or exit? (restart/exit): ")
    if choice.lower() != 'restart':
        break
