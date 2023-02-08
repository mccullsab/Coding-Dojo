from w1d3.human import Human

class Rogue(Human):
    def __init__(self, name, health=70):
        super().__init__(name, health)
        self.dodge = 10
    
    def poison(self, enemy):
        enemy.health -= 20
        print(f"[POISON] {self.name} poisons {enemy.name} for 20 dmg they now have {enemy.health} hp")