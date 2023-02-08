from w1d3.human import Human

class Paladin(Human):
    def __init__(self, paladin_name):
        #interetence - super means clal my parents/call my super class
        super().__init__(paladin_name, 80)
    
    #polymorphism
    def defend(self, damage):
        self.health -= (damage + 50)
        print(f"[DEFEND] {self.name} takes {damage} dmg and they now have {self.health}")

    def heal(self):
        self.health += 1000
        print(f"{self.name} heals for 10 hp and they now have {self.health}")