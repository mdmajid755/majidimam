import random


class Player:
    total_credits = 100

    def add(self, credits):
        self.total_credits += int(credits)
        return self

    def sub(self, credits):
        self.total_credits -= int(credits)
        return self

    def get_credit(self):
        return self.total_credits


class Dice:
    def roll(self):
        return random.randint(1, 6)


class Roll:
    wager = None
    has_won = False

    def set_wager(self, wager):
        self.wager = wager

    def roll(self):
        dice_roll = Dice().roll() + Dice().roll()
        print("You rolled " + str(dice_roll) + " points")
        if dice_roll == 7 or dice_roll == 11:
            print("You won to roll!")
            self.has_won = True
            return self
        if dice_roll == 2 or dice_roll == 3 or dice_roll == 12:
            print("You lost to roll :(")
            self.has_won = False
            return self
        return self.roll()


class Gameplay:
    player = None

    def exit(self):
        print("You have " + str(self.player.total_credits) + " points bye bye")
        exit()

    def play(self):
        if self.player.total_credits >= 1000:
            print("You have " + str(self.player.total_credits) + " credits, you won!")
            print("The game will restart")
            self.start()
        if self.player.total_credits <= 0:
            print("You have " + str(self.player.total_credits) + " credits, you lost!")
            print("The game will restart")
            self.start()
        else:
            print("You have " + str(self.player.total_credits) + " credits")
        wager = input("Make your wager, it should not exceed " + str(
            self.player.total_credits) + " points (type exit for exit): ")

        if wager == 'exit':
            self.exit()
        if (not wager.isdigit()):
            print("You can only wager numbers")
            self.play()
        if (int(wager) > self.player.total_credits):
            print("You can not wager more than you have")
            self.play()
        if (int(wager) > self.player.total_credits):
            print("You can not wager more than you have")
            self.play()
        if (int(wager) <= 0):
            print("You can not wager less than 0")
            self.play()
        roll = Roll()
        roll.set_wager(wager)
        result = roll.roll()
        if result.has_won:
            self.player.add(roll.wager)
        else:
            self.player.sub(roll.wager)
        self.play()

    def start(self):
        self.player = Player()

        print("Welcome to the dice game!")
        print("You have " + str(self.player.total_credits) + " credits")
        user_input = input("Type 'play' to play or 'exit' for exiting: ")
        if user_input == 'exit':
            exit()
        if user_input == 'play':
            self.play()


Gameplay().start()
