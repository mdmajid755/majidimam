#Intro to Dice Game
print("Dice Game Challenge!")

#Enable random number generation and time, just for fun and suspense
import random
import time

#Gameplay
def DiceGame():
    points = 100
    
    while True:
        if points > 0 and points <1000:
            wager = int(input(f"You have {points} points. How much would you like to wager? "))
            while wager < 1 or wager > points:
                wager = int(input(f"Invalid wager. You have {points} points. How much would you like to wager? "))
            print("\nRolling the dice...")
            time.sleep(1)
    
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
    
            print("The values are:")
            print("Dice 1 =", dice1, "\nDice 2 =", dice2)
    
            if total in [7, 11]:
                points += wager
                print(f"You win {wager} points. You now have {points} points.")
            elif total in [2, 3, 12]:
                points -= wager
                print(f"You lose {wager} points. You now have {points} points.")
            else:
                print(f"You neither win nor lose. You still have {points} points.")
            if points >= 1000:
                print(f"Congratulations! You won with {points} points.")
                break
            elif points == 0:
                print(f"Sorry, you lost with {points} points.")
                break

#Allow user to play again or quit        
while True:
    DiceGame()
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() != "y":
        break