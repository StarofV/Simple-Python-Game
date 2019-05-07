# Written by ThePythonDoge. You can do anything with this code. It probably can be shortened to 10 lines. 
import random
import json

# Load that sexy cash!
with open('lastScore.json', 'r') as infile:
    inst = json.load(infile)

# Define that sexy cash!    
balance = inst['score'] 

# Double that sexy cash!
def invest(bal):
  chance = random.randrange(1,11)
  if chance < 5: # 10% chance.. I think
    bal = 2
    print(f"You now have {balance * 2}!")
    return bal
  else:
    bal = 0
    print(f"You lost everything... Now you have {bal}")
    return bal

# Pick up that sexy cash!
while True:
    try:
        number = random.randrange(1,10) # Change this value and I will call the FBI on you
        pick = input("Do you want to pick money? (input enter to instantly invest!)\n")
        if pick.lower() in ('y', 'yes'): 
          balance += number
          print(f"You caught {number} bucks.\nBalance = {balance}.")
        else:
          balance *= invest(balance)
    except KeyboardInterrupt:
        with open('lastScore.json', 'w') as outfile: # Save that sexy cash!
            data = {'score': balance}
            json.dump(data, outfile, sort_keys = True, indent = 4) # Make it neat!
        exit(2) # Kill that sexy process!

# Am I commenting correctly?
