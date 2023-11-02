import random

# change

def roll_dice():
    return random.randint(1, 6) + random.randint(1, 6)

def play_game(points):
    while points > 0:
        print(f"Your current points: {points}")
        wager = int(input("Enter your wager (1 to 100, or 0 to quit): "))

        if wager < 0 or wager > points:
            print("Invalid wager. Please bet between 1 and your current points.")
            continue

        if wager == 0:
            break

        dice_sum = roll_dice()
        print(f"Dice roll result: {dice_sum}")

        if dice_sum <= 7:
            print(" ")
            points -= wager
        else:
            print("You win!")
            points += wager

    print(f"Game over. Your final score: {points}")

if __name__ == "__main__":
    initial_points = 100
    print("Welcome to the Dice Game!")
    play_game(initial_points)