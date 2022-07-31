## if statement

is_hot = True
is_cold = True

# Python use indentation to denote which section belongs to which if statement
if is_hot & is_cold:
    print("This can't happen!") # Statement activates when both is_cold = True and is_hot = True
elif is_cold:
    print('It is a cold day.')
    print('Wear more clothes.') # Statement activates when only is_cold = True
elif is_hot:
    print('It is a hot day.')
    print('Drink a lot of water.')  # Statement activates when only is_hot = True
else:
    print('It is a lovely day.')    # Statement activates when none of the statements is activated
print('Enjoy your day.')    # Statement always activates


## Exercise
price = 10 ** 6
good_cred = False
if good_cred:
    down_pay = .1 * price
else:
    down_pay = .2 * price

print(f'The down payment is ${down_pay}.')