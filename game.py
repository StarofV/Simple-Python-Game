import random
def start():
  print('Hello! The objective of the game is to collect money')
  a = input("Do you want to play?")
  if a.lower() in ('y', 'yes'): #If user inputs one of the following, game starts with 0 money.
    Game(0)
def Game(money):
    number = random.randint(1,51) #generate a random number between 1 and 50 as money.
    pick = input("Do you want to pick money?")
    if pick.lower() in ('y', 'yes'): #If user wants to pick money, he will get the random "number" added to his current money.
      money = money+number
      print(f"You caught {number} bucks\nYou currently have {money} bucks")
      Game(money)
    else:
      invest = input("Want to double your earnings?")
      if invest.lower() in ('y', 'yes'): #You know what happens here..
        print(f"You just got {money}!")
        money *= 2 #Investment is doubling your money by "*= 2".
        Game(money) #Go back to picking money with the current value of money that you have.
start()