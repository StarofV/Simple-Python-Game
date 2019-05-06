# Written by ThePythonDoge. You can do anything with this code. It probably can be shortened to 10 lines. 
import random
import json

# Load that sexy cash!
with open('lastScore.json', 'r') as infile:
    inst = json.load(infile)
# Define that sexy cash!    
balance = inst['score'] 

# Double that sexy cash!
def invest(balance):
  balance *= 2
  print(f"You now have {balance}!")
  return balance

# Pick up that sexy cash!
while True:
    try:
        number = random.randint(1,51) # Change this value and I will call the FBI on you
        pick = input("Do you want to pick money? (input enter to instantly invest!)")
        if pick.lower() in ('y', 'yes'): 
          balance += number
          print(f"You caught {number} bucks\nYou currently have {balance} bucks.") # Good job. Might add 50% for a fail.
        else:
          balance += invest(balance)
    except KeyboardInterrupt:
        with open('lastScore.json', 'w') as outfile: # Save that sexy cash!
            data = {'score': balance}
            json.dump(data, outfile, sort_keys = True, indent = 4) # Make it neat!
        exit(2) # Kill that sexy process!

# Am I commenting correctly?
