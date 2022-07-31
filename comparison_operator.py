## Comparison Operator (>, >=, <, <=, ==, !=)
# Comparison operator returns boolean values.
# a == b: Returns True if a equal to b
# a != b: Returns True if a is not equal to b


# temp = 29
# if temp >= 30:
#     print('It is a hot day!')
# else:
#     print('It is not a hot day.')


# Exercise:
password = input('Please enter new password: ')

if len(password) <= 3:
    print('Password must have more than 3 characters. ')
elif len(password) > 20:
    print('Password can not have more than 20 characters.')
else:
    print('Password successfully updated.')
