# REVIEW OOP, classes, constructor
#classmethod, statcimethod

class Ninja:
    #belond to the class not instance
    all_ninjas = [] # not part of the constrctor / no self
    # constructor---
    def __init__(self, name, health, age, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        if Ninja.check_age(age):
            self.age = age
        else:
            return
        Ninja.all_ninjas.append(self) #whenever I create a ninja, make it known it the class - self = instance i created

    # ---methods--- everything with self means it is part of the instance
    def display_stats(self):
        print("name: " + self.name + " has " + str(self.health) + "hp")
    def eat_straw(self):
        self.health = self.health + 10
        print(f"{self.name} ate a strawberry and they now have {self.health}")
    def attack(self, other_ninja):
        # print(f"{self.name} is attacking {other_ninja.name}")
        # other_ninja.health -= 10
        # print(f"{other_ninja.name} gets attacked by {self.name} with 10 dmg\n they now have {other_ninja.health}")
        # other_ninja.health -= self.weapon.damage
        print(f"{self.name} used a {self.weapon.name} which used {self.weapon.damage}")
    # class methods-----
    """
    do not have access to the instance
    no self
    hey do not individually change any one instance
    can only be called from the class
    """
    @classmethod
    def party(cls):
        print(cls.all_ninjas[1].name) # this is a list of ninja objects
        for one_ninja in cls.all_ninjas:
            print(one_ninja.eat_straw())
        # print(Ninja.all_ninjas)

    # static method----
    """
    stationary
    no access to anything
    independent
    used for utility and validations
    access through the class
    """
    @staticmethod
    def check_age(age):
        is_valid = True
        if age < 18:
            is_valid = False
            print("You are not old enough to enter the dojo")
        return is_valid

#------other class--------
class Weapon:
    def __init__(self, data, durability=100):
        self.damage = data['damage']
        self.type = data['type']
        self.name = data['name']
        self.durability = durability
    

katana = {
    "damage": 20,
    "type": "melee",
    "name": "katana"
    }

lazers = {
    "damage": 200,
    "type": "range",
    "name": "lazers"
    }


weapon1 = Weapon(lazers)
# weapon1 = Weapon(100, "melee", "nunchucks")
# weapon2 = Weapon(5, "range", "crossbow")


ninja1 = Ninja("Abby", 100, 26, weapon1)
ninja2 = Ninja("Naruto", 50, 18, katana)
# ninja3 = Ninja("dude", 50, 10, "stick")

# ninja2.attack(ninja1)


Ninja.party()



# ninja2.display_stats()
# ninja1.attack(ninja2)
# ninja2.display_stats()


# ninja2.eat_straw()
# ninja2.display_stats()

