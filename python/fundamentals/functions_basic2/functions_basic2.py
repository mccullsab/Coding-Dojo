#1

def countdown(num):
    cd = []
    i = num
    while i >= 0:
        cd.append(i)
        i = i - 1
    return cd
countdown(5)
print(countdown(5))

#2

def print_and_return(a, b):
    print(a)
    return(b)

print(print_and_return(1, 2))

#3

def first_plus_length(food):
    return food[0] + len(food)

cheese = [1,2,3,4,5]
print(first_plus_length(cheese))

#4

def values_greater(list):
    list_new = []
    for i in range(len(list)):
        if (list[i] > list[2]):
            list_new.append(list[i])
    if(len(list_new)<2):
        return False
    print(len(list_new))
    return list_new

nums = [1, 3, 7, 10, -2, 4, 4]
print(values_greater(nums))

#5

def length_and_val(size, value):
    list_new = []
    while len(list_new) < size:
        list_new.append(value)
    return list_new

print(length_and_val(10, 2))
