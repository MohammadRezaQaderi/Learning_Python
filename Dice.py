import random

class Dice :
    def roll(self):
        return random.randint(0,9) , random.randint(0,9)
    

dice = Dice()

print(dice.roll())