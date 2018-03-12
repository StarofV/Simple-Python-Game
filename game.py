import random

balance = 0
while True:
    number = random.randint(1,51)
    pick = input("Do you want to pick money?")
    if pick.lower() in ('y', 'yes'): 
      balance += number
      print(f"You caught {number} bucks\nYou currently have {balance} bucks")
    else:
      invest = input("Want to double your earnings?")
      if invest.lower() in ('y', 'yes'): 
        print(f"You just got {balance}!")
        balance *= 2 