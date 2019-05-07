# Written by ThePythonDoge. You can do anything with this code. It probably can be shortened to 10 lines. 
import random, json

# Load that sexy cash!
with open('lastScore.json', 'r') as infile:
    inst = json.load(infile)

# Define that sexy cash!    
balance = inst['score'] 

# Double that sexy cash!
def invest(bal):
  chance = random.randrange(1,11) # 50% of winning
  bal = 2 if chance < 5 else 0
  print(f"You doubled to {balance * 2}!" if bal == 2 else "You lost everything...")
  return bal

# Pick up that sexy cash!
while True:
    try:
        number = random.randrange(1,10) #Change this value and I will call the FBI on you
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
