import random

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def main():
    player_points = 500 # Starting points for the player

    while player_points > 0 and player_points < 1000:
        print(f"You have {player_points} points.")
        
        wager = input("Enter your wager (1 to your points or 'exit' to quit): ")
        
        if wager.lower() == 'exit':
            break
        
        wager = int(wager)
        
        if wager < 1 or wager > player_points:
            print("Invalid wager. Please enter a valid wager.")
            continue
        
        roll = roll_dice()
        print(f"You rolled a {roll}")
        
        if roll in (7, 11):
            player_points += wager
            print(f"You win! You now have {player_points} points.")
        elif roll in (2, 3, 12):
            player_points -= wager
            print(f"You lose! You now have {player_points} points.")
    
    if player_points >= 1000:
        print("Congratulations! You've won the game!")
    else:
        print("Sorry, you've lost the game!")

if __name__ == "__main":
    main()