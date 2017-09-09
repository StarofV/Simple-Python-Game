import random
money = 0
def start():
  print('Hello! The objective of the game is to collect money')
  a = input("Do you want to play?")
  if a.lower() in ('y', 'yes', 'Y'):
    Game()
def Game():
    global money 
    number = random.randint(1,50)
    pick = input("Do you want to pick money?")
    if pick.lower() in ('y', 'Y', 'yes'):
      money = money+number
      print(f"You caught {number} bucks\n You currently have {money} bucks")
      Game()
    else:
      invest = input("Want to double your earnings?")
      if invest.lower() in ('y', 'yes'):
        print(f"You just got {money} !")
        money *= 2 
        Game()
start()
