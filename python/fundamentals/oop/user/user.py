class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        return self
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200
        return self
    def spend_points(self, amount):
        self.gold_card_points -= amount
        return self

#Chaining Methods BELOW

matt = User("Matt", "Vasseur", "matt@gmail.com", 27)
matt.display_info().enroll().spend_points(50).display_info()

abby = User("Abby", "M", "abby@gmail.com", 27)
abby.enroll().spend_points(50).display_info()


#USER BELOW

matt = User("Matt", "Vasseur", "matt@gmail.com", 27)

matt.enroll()
print(matt.is_rewards_member)
print(matt.gold_card_points)
matt.spend_points(10002)
print(matt.gold_card_points)
# print(matt.is_rewards_member(50))

abby = User("Abby", "M", "abby@gmail.com", 27)
print(abby.gold_card_points)
print(abby.display_info())
