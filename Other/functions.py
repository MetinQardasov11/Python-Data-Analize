# #return 'goodbye'when the function is called
def good_bye():
    return 'goodbye'

say_something = good_bye()
print(say_something)

#----------------------------------------------------------------

def say_salamunaleykum():
    print('salamun aleykum')
# say_salamunaleykum()

#----------------------------------------------------------------

def show_tree():
    picture = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0],
    ]

    for image in picture:
        for pixel in image:
            if pixel == 1:
                print('*',end='')
            else:
                print(' ',end='')
        print('')

# show_tree()

#----------------------------------------------------------------

# Default parameters and keyword arguments
def say_something(name='Ali',emoji='💪'):
    print(f'Salamun Aleykum {name} {emoji}')

# say_something()
# say_something('Metin','👨‍💻')
# say_something('Omar','🫡')
# say_something('Osman','🥺')
# say_something(emoji='🤩',name='Isa')
# say_something(name='Ebubekir')

#----------------------------------------------------------------

# return 

def sum_num(num1,num2):
    return num1 + num2

print(sum_num(1,4))
total = sum_num(10,20)
print(sum_num(10,sum_num(10,total)))

def sum_num(num1,num2):
    def another_func(num1, num2):
        return num1 + num2
    return another_func(num1, num2)
print(sum_num(12,12))


def sum_num(num1,num2):
    def another_func(num1,num2):
        def another_another_func(num1,num2):
            return num1 + num2
        return another_another_func(num1,num2)
    return another_func(num1,num2)

print(sum_num(12,32))

#----------------------------------------------------------------

# Task 

# 1
def checkDriverAge():
    age = int(input('Enter the age of the driver: '))
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge()

# 2
def checkDriverAge(age=0):
    
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

# checkDriverAge(92)

#----------------------------------------------------------------

# Docstring

def test(a):
    '''
    Info: this function tests nd prints param a
    '''
    print(a)
print(test.__doc__)

#----------------------------------------------------------------

def is_even(num):
    if num % 2 == 0:
        return True
    elif num % 2 == 1:
        return False
print(is_even(10))

# OR

def is_even(num):
    if num % 2 == 0:
        return True
    return False
print(is_even(51))

# OR
def is_even(num):
    return num % 2 == 0
print(is_even(22))

#----------------------------------------------------------------

# Rule: params, *args, default params, **kwargs

# *args -> tuple
def super_func(*args):
    print(args)
    return sum(args)

print(super_func(1,2,3,4,5))

# kwargs -> dictionary
def func(*args,**kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(func(1,2,3,4,5,num1=1,num2=2,num3=3,num4=4))

#----------------------------------------------------------------

def highest_even(lis):
    evens = []
    for i in lis:
        if i % 2 == 0:
            evens.append(i)
    # max_num = 0
    # for even in evens:
    #     if even > max_num:
    #         max_num = even
    # return max_num
    
    # OR
    return max(evens)
            
print(highest_even([100,22,50,72,27,19,63,73,62,98]))

#----------------------------------------------------------------

# Scope -> what variables do I have access to?

# 1 -> Start a local
# 2 -> Parent local
# 3 -> Global
# 4 -> Built in Python functions
a = 1
def confusion():
    a = 5
    return a
print(a)
print(confusion())

def parent():
    a = 10
    def child():
        return a
    return child()
print(parent())
print(a)

#----------------------------------------------------------------

# global keywords

total = 0
def count():
    global total
    total = total + 1
    return total

# count()
print(count())

def count(total):
    total += 1
    return total

print(count(count(count(total))))

#----------------------------------------------------------------

# nonlocal keyword
def outer():
    x = 'local'
    def inner():
        nonlocal x
        x = 'nonlocal'
        print('Inner :',x)
    inner()
    print('Outer :',x)
# outer()

#----------------------------------------------------------------

def multiply_by(li):
    new_list = []
    for item in li:
        new_list.append(item*2)
    return new_list
print(multiply_by([1,2,3,4]))

#----------------------------------------------------------------

# map
my_list = [10,20,30,40,50]
def multiply_by_2(item):
    return item * 2
print(list(map(multiply_by_2,[1,2,3,4,5])))
print(list(map(multiply_by_2,my_list)))


email = [
    'm1@gmail.com',
    'm2@gmail.com',
    'm3@gmail.com'
]
def make_upper(item: str):
    return item.upper()
print(list(map(make_upper,email)))

#----------------------------------------------------------------

# filter
my_list = [1,2,3,4,5]
def check_odd(item):
    return item % 2 != 0
print(list(filter(check_odd,my_list)))

#----------------------------------------------------------------

# zip
my_list = [1,2,3,4,5]
your_list = [10,20,30,40,50]
their_list = (5,4,3,2,1)
print(list(zip(my_list,your_list,their_list)))

#----------------------------------------------------------------

# reduce
from functools import reduce
my_list = [1,2,3,4,5] 
def accumlator(acc, item):
    print(acc, item) 
    return acc + item
print(reduce(accumlator,my_list,1)) # burda 1-in yerine istediyimiz reqemi yaza bilerik.

# burda 1 1
#       2 2
#       4 3
#       7 4
#       11 5
#       16

#----------------------------------------------------------------

# List comprehension
my_list_new = []
for i in 'Hello':
    my_list_new.append(i)
print(my_list_new)

# OR
my_list_new = [char for char in 'Salamun Aleykum']
print(my_list_new)

my_list2 = [num for num in range(1,100)]
print(my_list2)
my_list3 = [num*2 for num in range(1,10)]
print(my_list3)
my_list4 = [num**2 for num in range(1,100) if num % 2 == 0]
print(my_list4)

#----------------------------------------------------------------

# Set comprehension
my_list_new = {char for char in 'Salamun Aleykum'} 
# tekrarlananlari cixarmayacaq. qalanlarini da her defe random yerdeyisme edecek
print(my_list_new)
my_list2 = {num for num in range(1,100)}
print(my_list2)
my_list3 = {num*2 for num in range(1,10)}
print(my_list3)
my_list4 = {num**2 for num in range(1,100) if num % 2 == 0}
print(my_list4)

#----------------------------------------------------------------

# dict comprehension
simple_dict = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
    'd' : 4
}
my_dict = {key:value**2 for key,value in simple_dict.items()}
print(my_dict)
my_dict_new = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}
print(my_dict_new)
my_dict_2 = {num:num*2 for num in [1,2,3,4,5]}
print(my_dict_2)

#----------------------------------------------------------------

some_list = ['a', 'b', 'c', 'b', 'd','m', 'n', 'n']
duplicates = list(set([value for value in some_list if some_list.count(value) > 1]))
print(duplicates) 