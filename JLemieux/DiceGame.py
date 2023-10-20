#Random number generator
import random

#Rolling 2 dice and returning values 1 through 6
def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

#The game
def play_game():
    points = 100
    while points > 0 and points < 1000:
        print("Lemieux's High Rolling 7/11 Casino")
        print(f'Points: {points}')
        #Defines wager as the user input
        wager = input(f'Enter a wager (1-{points}), or type "EXIT" to cash out: ')
        
        if wager.upper() == "EXIT":
            break
        
        #Converts wager to an integer
        wager = int(wager)
        
        #Can't be 0 or more than the amount of points you have
        if wager < 1 or wager > points:
            print("Invalid wager. Please enter a valid wager.\n")
            continue
        
        #The two numbers from randomization become both dice rolls
        dice1, dice2 = roll_dice()
        #Total adds both rolls
        total = dice1 + dice2
        print(f'\nDice rolls: {dice1}, {dice2}\n')
        if total in [7, 11]:
            #Adds wager to point total
            points += wager
            print(f'You won with a {total}! Points +{wager}\n')
        elif total in [2, 3, 12]:
            #Subtracts wager from total
            points -= wager
            print(f'You lost with a {total}! Points -{wager}\n')
        else:
            print(f'You rolled a {total}... Nothing. Roll again!\n')
    #If you win
    if points >= 1000:
        print(f'Congratulations! You won with {points} points.\n')
    #If you exit the game
    elif wager == "EXIT":
        print(f'\nYou walked away with {points} points\n')
    #If you have 0 points and lose
    else:
        print(f'You lost with {points} points.')

def main():
    while True:
        play_game()
        choice = input('Do you want to play again? (yes/no): ')
        #If no is entered, break. If yes is entered then the while loop keeps running and plays again
        if choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
