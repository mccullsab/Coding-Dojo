#OOP
    #capitalize classes in order to denote it

#object = instance of a class
#class = blueprint for our instances (object)

#below = inneffiecient, use oop

dog1 = {
    'name': 'Cinanmon',
    'age': 7,
    'color': 'orange'
}

dog2 = {
    'name': 'Spot',
    'age': 5,
    'breed': 'lab'
}

#---CREATE A CLASS----

class Dog:
    #constructor - creates defaults and builds the class
    def __init__(self, name, age, breed):
        #dunder init is the initialize with the double underscore
        #self is like this in javascript
        self.age = age
        self.name = name
        self.breed = breed
        #need to add the self in order to declare that these attributes are a part of the instance

doggo1 = Dog("spot", 5, "lab")
dog2 = Dog("maisy", 20, "wheaten")
print(doggo1)
#prints the object that has been instantiated
print(doggo1.name, doggo1.age, dog2.breed)
print(dog2.name)

#----METHODS----

class Dog:
    def __init__(self, name, age, breed = "wheaten"):
        #default values need to be put at the end of the arguements
        self.age = age
        self.name = name
        self.breed = breed
        # print(self)
    def bark(self):
        #all methods that are instance methods take in self
        print(f"{self.name} makes a loud bark!!!!")
    def birthday(self):
        #employer preference below
        self.age = self.age + 1
        print(f"{self.name} is {self.age} old")

    def __repr__(self):
        #rename the default instance name
        return f"{self.name} is a {self.breed}"

doggo1 = Dog("spot", 5, "lab")
print(doggo1)
doggo2 = Dog("rex", 10)
print(doggo2)

doggo1.birthday()
doggo1.birthday()
doggo1.birthday()
doggo1.birthday()
