for item in 'Metin Qardasov':
    print(item)

#----------------------------------------------------------------

for item in [1,2,3,4,5]:
    print(item)

#----------------------------------------------------------------
    
for item in {1,2,3,4,5}:
    print(item)
print(item)

#----------------------------------------------------------------

for i in [1,2,3]:
    for j in ['a', 'b', 'c']:
        print(i,'<->', j)
        
#----------------------------------------------------------------

# iterable can be -> list, tuple, dictionary, set, string
# iterate -> one by one check each item in the collection
# for i in x <- x is iterable 

user = {
    'name' : 'Metin',
    'age' : 20,
    'Programming Language': 'Python'
}

for item in user:
    print(item)
    
for key,value in user.items():
    print(key, ':', value)
    
for item in user.keys():
    print(item)
    
for item in user.values():
    print(item)

#----------------------------------------------------------------

my_list = [1,2,3,4,5,6,7,8,9,10]
sum_num = 0
for i in my_list:
    sum_num += i
print(sum_num)

#----------------------------------------------------------------

# range()
print(range(100))
print(range(0,100))

for num in range(10):
    print(num)
    
for _ in range(0,15,2):
    print(_)
    
for _ in range(10,0,-1):
    print(_)
    
for _ in range(10,0,-2):
    print(_)

for _ in range(0,5):
    print(list(range(11)))

#----------------------------------------------------------------

# enumerate

for i,char in enumerate('Metin'):
    print(i,char)
    
for i,char in enumerate([1,2,3,4,5]):  # enumerate(can be list,tuple,str,set)
    print(i,char)
    
for i,num in enumerate(list(range(100))):
    if num == 50:
        print(f'index of {i} is {num}')
    print(i,num)

#----------------------------------------------------------------

# while

i = 0
while i < 20:
    print(i)
    i += 1
else:
    print('Loops are done!!!...')

my_list = [1,2,3,4,5]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

    
while True:
    response = input('Say something: ')
    if response == 'ok':
        break

#----------------------------------------------------------------

# break
i = 0
while i < 50:
    if i == 20:
        break
    print(i)
    i += 1


# continue
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue


# pass
for i in my_list:
    pass
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    pass

# Task
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


#----------------------------------------------------------------

some_list = ['a', 'b', 'c', 'b', 'd','m', 'n', 'n']
duplicates = []

for letter in some_list:
    if some_list.count(letter) > 1:
        if letter not in duplicates:
            duplicates.append(letter)
print(duplicates)
