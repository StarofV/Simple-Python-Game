# Written by ThePythonDoge. You can do anything with this code. It probably can be shortened to 10 lines. 
import random, json

# Load that sexy cash!
with open('lastScore.json', 'r') as infile:
    inst = json.load(infile)    
    balance = inst['score'] 

# Double that sexy cash!
def invest(bal):
  chance = random.choice([True, False]) # 50% of winning
  bal = 2 if chance == True else 0
  print(f"You doubled to {balance * 2}!" if bal == 2 else "You lost everything...")

  return bal

# Pick up that sexy cash!
while True:
    try:
        pick = input("Do you want to pick money? (input enter to instantly invest!)\n")
        pick_chance = random.choice([True,False])
        
        if pick.lower() in ('y', 'yes') and pick_chance == True: 
          number = random.randrange(1,11)
          balance += number
          print(f"You caught {number} bucks.\nBalance = {balance}.")
        
        elif pick.lower() in ('y', 'yes') and pick_chance == False:
          print("Oh no, you didn't catch any. Try again!")
        
        else:
          balance *= invest(balance) # multiply the number returned
    
    except KeyboardInterrupt: #Save and exit
        with open('lastScore.json', 'w') as outfile:
            data = {'score': balance}
            json.dump(data, outfile, sort_keys = True, indent = 4) # Make it neat!
        exit()
