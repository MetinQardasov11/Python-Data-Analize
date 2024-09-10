# Data types
print(round(3.121,2))
print(abs(-2132))

#--------------------------------------------------------------------------------------------------

print(bin(13))
print(hex(130))
print(int('0b10110',2))
print(int('0x82',16))

#--------------------------------------------------------------------------------------------------

a,b,c = 12,2,9
print(a)
print(b)
print(c)

#--------------------------------------------------------------------------------------------------

value = 5
value -= 2
value *= 4
print(value)

#--------------------------------------------------------------------------------------------------

username = 'supercoder'
password = 'supersecret'
long_string = '''
W O W
O   O
-----
'''
print(long_string)

first_name = 'Metin'
last_name = 'Qardasov'
full_name = first_name + ' ' + last_name
print(full_name)

#--------------------------------------------------------------------------------------------------

# Escape Sequence
weather = "It\'s a \"kind of\" weather"
weather = "It\\s a \"kind of\" weather"
weather = "\t It\'s a \"kind of\" weather"
weather = "\t It\'s a \"kind of\" weather \n I hope you will be able to see it..."
print(weather)

#--------------------------------------------------------------------------------------------------

name = 'Metin'
age = 20
print('Hi ' + name + '. You\'re ' + str(age) + ' years old.')
print(f'Hi {name}. You\'re {age} years old.')
print('Hi {}. You\'re {} years old'.format(name, age))
print('Hi {1}. You\'re {0} years old'.format(age,name))

#--------------------------------------------------------------------------------------------------

selfish = 'me me me'
#          01234567
print(selfish[0])
print(selfish[1])

nums = '12345678'
# '[start : stop : stepover]'
print(nums[2:6])
print(nums[0:8:2])
print(nums[3:])
print(nums[:4])
print(nums[::2])
print(nums[-5])
print(nums[-1])
print(nums[::-1])
print(nums[::-2])

nums = nums + '8'
print(nums)

#--------------------------------------------------------------------------------------------------

greet = 'Salamun Aleykum'
print(greet[:len(greet)])

quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('or'))
print(quote.replace('be','me'))

#--------------------------------------------------------------------------------------------------

# birth_year = int(input('What year were you born? '))
# age = 2024 - birth_year
print(f'Your age is {age}')

#--------------------------------------------------------------------------------------------------

# username = input('Username: ')
password = input('Password: ')

password_length = len(password)
hidden_password = password_length * '*'
print(f'Your username is {username}, password is {hidden_password}, length of password is {len(password)}')

#--------------------------------------------------------------------------------------------------

li = [1,2,3,4,5,6]
li_2 = ['a', 'b', 'c', 'd', 'e']
li_3 = [1,2,'a',True,3.5]
amazon_cart = [
    'sun glasses', 
    'notebooks',
    'apples',
    'grapes',
    'toys',
    'accessories'
    ]
length = len(amazon_cart)
print(length)
print(amazon_cart[0])
print(amazon_cart[len(amazon_cart)-1])
print(amazon_cart[0::2])

amazon_cart[2] = 'watches'
print(amazon_cart)

# new_cart = amazon_cart
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)

#--------------------------------------------------------------------------------------------------

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrix[0][2])

#--------------------------------------------------------------------------------------------------

baskets = [1,2,3,4,5]
new_baskets = baskets.append(6)
print(baskets)

nums = [10,20,30,40]
new_nums = nums.insert(2,200)
print(nums)

lis = [1,3,5,7,9]
new_lis = lis.extend([11,13,15])
print(lis)

pop = lis.pop()
pop = lis.pop(2)
print(lis)

remove = lis.remove(13)
print(lis)

clear = lis.clear()
print(lis)

num_list = [1,5,2,7,3,10,4,6]
str_list = ['a','f','g','m','z','q','r','f']
find_index_num = num_list.index(4)
find_index_str = str_list.index('m',0,5) # return 3. Because m is available in 0 and 5 intervals
# find_index_str = str_list.index('m',0,2) # return error. Because m is not available in 0 and 2 intervals
print(find_index_num)
print(find_index_str)
print('x' in str_list)
print('f' in str_list)
print('i' in 'Metin Qardasov')
print(str_list.count('f'))

# str_list.sort()
print(str_list)
print(sorted(str_list))

new_str_list = str_list[:]
new_str_list.sort()
print(str_list)
print(new_str_list)

str_list.reverse()
print(str_list)

#--------------------------------------------------------------------------------------------------

character = ' | '
sentences = character.join(['salamun','aleykum','my','name','is','Metin'])
print(sentences)

# OR

sentences = ' '.join(['salamun','aleykum','my','name','is','Metin'])
print(sentences)

#--------------------------------------------------------------------------------------------------

a,b,c, *other = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(b)
print(c)
print(other)

no_value = None
print(no_value)

#--------------------------------------------------------------------------------------------------

dictionary = {
    'a' : 1,
    'b' : 2
}

print(dictionary)
print(dictionary['a'])

dictionary_2 = {
    'a' : [1,2,3],
    'b' : 'hello world',
    'c' : True
}
print(dictionary_2['a'])
print(dictionary_2['a'][2])

dict_list = [
    {
        'a' : [1,2,3],
        'b' : 'Salamun Aleykum',
        'c' : True    
    },
    {
        'a' : [4,5,6],
        'b' : 'How are you?',
        'c' : False
    },
    {
        'a' : [7,8,9],
        'b' : 'Elhamdulillah',
        'c' : [True, False]
    }
]
print(dict_list[0]['b'])
print(dict_list[1]['a'][2])

user = {
    'basket' : [1,2,3],
    'greet' : 'Hello',
    'age' : 30
}
print(user.get('fruits',['apple','orange','banana']))
print(user.get('age',55))

user2 = dict(name = 'Metin')
print(user2)

print('age' in user)
print('basket' in user.keys())
print('name' in user.values())
print('hello' in user.items())
print(user.items())

user_2 = user.copy()
user_2.clear()
print(user)
print(user_2)

print(user.pop('age'))
print(user.popitem())
user.update({'age' : 20})
user.update({'ages' : [20,50,60]})
print(user)

#----------------------------------------------------------------------------------------------------------------------

my_tuple = (1,2,3,4,5,5)
print(my_tuple[2])
print(5 in my_tuple)

user = {
    (1,2) : [1,2,3],
    'greet' : 'Salam Aleykum',
    'age' : 20
}
print(user[(1,2)])

new_tuple = my_tuple[1:4]
print(new_tuple)

x,y,z,*other = (1,2,3,4,5,6,7,8,9,10,11,12)
print(x)
print(y)
print(z)
print(other)

print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

#----------------------------------------------------------------------------------------------------------------------

my_set = {1,2,3,4,5,5}
my_set.add(67)
my_set.add(3)
print(my_set)

my_list = [1,2,3,4,5,5]
print(set(my_list))

print(1 in my_set)
print(len(my_set))
print(my_set)

new_set = my_set.copy()
new_set.clear()
print(new_set)
print(my_set)

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8,9,10}

print(set_1.difference(set_2)) # set_1-in set_2-den ferqli olanlari
print(set_2.difference(set_1)) # set_2-in set_1-den ferqli olanlari

# set_1.discard(5) # set_1-de 5-i silmek
print(set_1)

set_1.difference_update(set_2) # Ortaq olmayanlari tapmaq set_1 ucun
print(set_1) 

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8,9,10}

print(set_1.intersection(set_2)) # Ortaq olanlari tapmaq
# OR
print(set_1 & set_2) # Ortaq olanlari tapmaq
print(set_1.isdisjoint(set_2)) # Ust uste dusurmu?

print(set_1.union(set_2)) # Birlesdirmek
# OR
print(set_1 | set_2) # Birlesdirmek

set_1 = {4,5}
set_2 = {4,5,6,7,8,9,10}
print(set_1.issubset(set_2)) # Alt coxluq
print(set_2.issuperset(set_1)) # set_2 set_1-in super coxlugudurmu?


is_friend = True
is_User = False
if is_friend and is_User:
    print('Best friend forever')
    
if is_friend or is_User:
    print('Friend forever')

print('hello' == 'hello')
print('b' < 'a')
print('e' < 'z')
print('a' > 'A')
print(1 < 2 < 3 < 4 < 5)
print(4 > 5 < 1 < 2)
print(not True)
print(not 1 == 1)
print(not 3 <= 2)