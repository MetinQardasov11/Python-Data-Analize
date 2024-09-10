is_old = False
is_licenced = False

if is_old:
    print('you are old enough to drive!')
print('checheck')


if is_old:
    print('If')
elif is_licenced:
    print('Elif ')
else:
    print('Else')

#----------------------------------------------------------------------------------------------------------------------

# Ternary operations
# candition_if_true if condition else condition_if_false

is_friend = True
is_friend = False
can_message = 'message allowed' if is_friend else 'message not allowed'
print(can_message)

#----------------------------------------------------------------------------------------------------------------------

is_magician = True
is_expert = False

if is_magician and is_expert:
    print('You are a master magician!')
elif is_magician and not is_expert:
    print('At least you are getting there')
elif not is_magician:
    print('You need magic powers')

#----------------------------------------------------------------------------------------------------------------------

print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])
print('-------------------')
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([1,2,3] is [1,2,3])

a = [4,5,6]
b = [4,5,6]
print(a == b)
print(a is b)