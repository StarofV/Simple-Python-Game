import random
def start():
  print('Hello! The objective of the game is to collect money')
  a = input("Do you want to play?")
  if a.lower() in ('y', 'yes'):
    Game()
def Game(money):
    number = random.randint(1,50)
    pick = input("Do you want to pick money?")
    if pick.lower() in ('y', 'Y', 'yes'):
      money = money+number
      print(f"You caught {number} bucks\n You currently have {money} bucks")
      Game(money)
    else:
      invest = input("Want to double your earnings?")
      if invest.lower() in ('y', 'yes'):
        print(f"You just got {money} !")
        money *= 2 
        Game(money)
start(0)
