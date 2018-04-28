# HyperNovae
import random
import json

with open('lastScore.json', 'r') as infile:
    inst = json.load(infile)
balance = inst['score'] 

def invest(balance):
  balance *= 2
  print(f"You now have {balance}!")
  return balance
while True:
    try:
        number = random.randint(1,51)
        pick = input("Do you want to pick money? (input enter to instantly invest!)")
        if pick.lower() in ('y', 'yes'): 
          balance += number
          print(f"You caught {number} bucks\nYou currently have {balance} bucks")
        else:
          balance += invest(balance)
    except KeyboardInterrupt:
        with open('lastScore.json', 'w') as outfile:
            data = {'score': balance}
            json.dump(data, outfile, sort_keys = True, indent = 4)
        exit(2)
