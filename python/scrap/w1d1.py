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
