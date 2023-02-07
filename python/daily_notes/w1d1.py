#Primative vars
bool = True
my_num = 6
float_num = 3.6
string = "john"
formatted_string = f"we can inject {bool}"
print(formatted_string)
concat_string = "my number is " + str(my_num)
print(concat_string)

#Composite types
    #lists - arrays in JS, hold a collection of primative data
my_list = [1,2,3,4,5]
my_list[1]
my_list.append(1337)
print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort(reverse=True)
print(my_list)
    #dictionaries - objects in JS, dont have an index, have key value pairs, coma seperated
dog_dict = {
    "name": "Mochi",
    "age": 3,
    "breed": "Corgi",
    "is_a_good_girl": True,
    # "name": "Rex"
}
print(dog_dict)
print(dog_dict["name"])
dog_dict['name'] = "Abby"
print(dog_dict)
# print(dog_dict['size']) #error
print(dog_dict)

    #tuples - similar to a list but can not be changed, indexed
tup = (11, 12, 33, "bob")
print(tup[0])


#------considitional------
#if
#elif
#else

x = 1
if x == 5:
    print('x is 5')
elif x>5:
    print('no')
else:
    print('nahhh')

#loops
#for loops

# for __itertor__ in __collection__ : "loop iterator in each one of the collection and print it"
# range() - function that return a sequence of nubers
# range()

end = 10
for i in range(1,end+1):
    print(i)

# 2-10, step by 2
for i in range(2, 10+1, 2):
    print(i)

# 10->5
for i in range(10,5-1,-1):
    print(i)

for element in range(10):
    print(element)

#loop over a string
for x in 'Hello':
    print(x)

#iterate over a list
food_list = ['pizza','cheese','ramen','sushi','more cheese']
print(food_list)

for i in range(len(food_list)):
    print(food_list[i])

for item in food_list:
    print(item)


#dictionaries

cat1 = {
    'name': 'Cinanmon',
    'age': 7,
    'color': 'orange'
}

print(cat1['name'])

cat2 = {
    'name': 'Bunny',
    'age': 2,
    'color': 'black'
}

print(cat2['name'])

#print a list with the 2 elements
cat_list = [cat1, cat2]
print(cat_list)

#get info from all lists
for singlelist_cat in cat_list:
    # print(singlelist_cat)
    for key in singlelist_cat:
        print(singlelist_cat[key])

#print keys
for key in cat2:
    print(key)

#print key space info
for key in cat2:
    print(key, cat2[key])


capitals = {
    "Washington":"Olympia",
    "California":"Sacramento",
    "Idaho":"Boise",
    "Illinois":"Springfield",
    "Texas":"Austin",
    "Oklahoma":"Oklahoma City",
    "Virginia":"Richmond"}

#just get the values
for val in capitals.values():
    print(val)

for state_key, state_capital in capitals.items():
    print(state_key, state_capital)


#functions are a set of instructions (recipe), repeatable, can take parameters, will ALWAYS return something
#define your functions with verbs
#A FUNCTION IS EQUAL TO ITS RETURN

def greeting():
    print("hello ninja!")

greeting()

def say_hello(name, times=0):
    for i in range(times):
        print(f"Hello {name}")

say_hello("bob", 3)
#above - 0 is the default but the 3 arguement will always override it



