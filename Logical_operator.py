## Logical Operators

high_income = False
good_cred = True

if high_income and good_cred:   # Logical and operator, can also use &. The bool value is True for A & B iff A and B are both True
    print('Fully eligible for loan.')
elif high_income or good_cred:  # Logical or operator, can also use |. The bool value is True for A | B iff at least one statement among A, B is True
    print('Probably eligible for loan.')
else:
    print('Sorry. Not eligible for loan.')

# Notes:
# and: true if both true [&]
# or: true if at least one true [|]
# not: reverse boolean value (True to False, False to True)