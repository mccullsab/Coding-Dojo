num1 = 42 # var declaration, num
num2 = 2.3 # var, float
boolean = True # var, bool
string = 'Hello World' #var, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #var, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #var, dict
fruit = ('blueberry', 'strawberry', 'banana') #var, tuple
print(type(fruit)) #tuple
print(pizza_toppings[1]) #sausage
pizza_toppings.append('Mushrooms') #mush to the end of pt list
print(person['name']) #john
person['name'] = 'George' #john changes to george
person['eye_color'] = 'blue' #adds new item to dict
print(fruit[2]) #banana

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# its lower 

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
    #just right!

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

"""
0
1
2
3
4
2
3
4
2
5
8
0
1
2
3
4
"""

pizza_toppings.pop() # olives out
pizza_toppings.pop(1) #sausage out

print(person) #same but george and eyecolor
person.pop('eye_color') #removes eyecolor
print(person) #removes eyecolor

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

    # after 1st 3 times

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times() #10 times printed

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #4 times pritned

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)
#14 


"""
Bonus section
"""

# # print(num3) #error
# num3 = 72 
# # fruit[0] = 'cranberry' #error
# person['favorite_team'] = 'Cubs'
# print(person) # error
print(pizza_toppings[7]) #error
print(boolean) #true
# fruit.append('raspberry') #error
# fruit.pop(1) #error