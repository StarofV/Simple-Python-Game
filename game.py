# HyperNovae
import random

balance = 0
def invest(balance):
  balance *= 2
  print(f"You now have {balance}!")
  return balance
while True:
    number = random.randint(1,51)
    pick = input("Do you want to pick money? (input enter to instantly invest!)")
    if pick.lower() in ('y', 'yes'): 
      balance += number
      print(f"You caught {number} bucks\nYou currently have {balance} bucks")
    else:
      balance += invest(balance)
