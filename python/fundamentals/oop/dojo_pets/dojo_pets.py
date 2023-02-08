class Ninja:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food
    
    def walk(self):
        print(f"{self.first_name} is taking {self.pet.name} on a walk\n their play is activated: {self.pet.play()}")
    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name} resulting in {self.pet.eat()}")
    def bathe(self):
        print(f"{self.pet.name} says {self.pet.noise()}!")

class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
    
    def sleep(self):
        self.energy += 10
        print(f"{self.name} has sleep extra energy new energy is {self.energy}")
    def eat(self):
        print("Yum food!")
        self.energy += 5
        self.health += 10
        return f"{self.energy} energy and {self.health} health"
    def play(self):
        self.energy -= 10
        self.health += 50
        return f"{self.name} has play energy drain new energy is {self.energy} and {self.health} health"
    def noise(self):
        return "woof!"

maisy = Pet("maisy", "wheaten", "spin", 100, 100)
abby = Ninja("abby", "M", maisy, 2, "pure")

abby.feed()
abby.walk()
abby.bathe()

# abby.feed()
# maisy.play()







