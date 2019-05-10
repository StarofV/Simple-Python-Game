# Written by ThePythonDoge. You can do anything with this code. It probably can be shortened to 10 lines.
import random
import json

# Load that sexy cash!


class Tree():
    def __init__(self, balance):
        self.balance = balance

    def chance(self):
        chance = random.choice([True, False])  # 50% chance
        return chance

    def run(self):
        while True:
            try:
                pick = input("Type 'y' or 'yes' to shake the tree! Press 'enter' to double money!\n")

                if pick in ('y', 'yes') and self.chance == True:
                    number = random.randrange(1, 11)
                    self.balance += number
                    print(f"{number} fell! You got {self.balance} now.")
                elif pick.lower() in ('y', 'yes') and self.chance == False:
                    print("Oh no. No cash fell!")
                elif self.chance == True:
                    self.balance *= 2
                    print(f"You doubled your money to {self.balance}")
            except KeyboardInterrupt:
                with open('lastScore.json', 'w') as outfile:
                    data = {'score': self.balance}
                    json.dump(data, outfile, sort_keys = True, indent = 4) # Make it neat!
                exit()


def main():
    with open('lastScore.json', 'r') as infile:
        inst = json.load(infile)
        money = inst['score']
    game = Tree(money)
    game.run()
main()
