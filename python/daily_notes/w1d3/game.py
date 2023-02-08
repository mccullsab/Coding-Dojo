from w1d3.paladin import Paladin
from w1d3.rogue import Rogue
import random 

shadow = Rogue("Shadow")
bob = Paladin("bob")

while shadow.health > 0 and bob.health > 0:
    print("you are the great paladin, you approach a rogue!")
    response = ""

    while not response == "1" and not response =="2":
        response = input("What do you do?\n 1. attack?\n or health\n")
        if response == "1":
            bob.attack(shadow)
        elif response == "2":
            bob.heal()
        else:
            print(">>> please choose a valid option")
        
        #CPU
        dice_roll = print(random.randint(1,2))
        if dice_roll == 1:
            shadow.attack(bob)
        else:
            shadow.poison(bob)

#end game
if bob.health > 0:
    print("you won!")
else:
    print("The rogue won!")

    