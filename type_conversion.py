## Datatyoe Conversion
# birth_year = input('Birth year: ')
# age = 2022 - birth_year  # Operation must be done between same data types! 2022 - '1998', won't work
# print(age)

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2022 - int(birth_year)    # Operation between int and float is allowed and returns a float variable
# print(type(age))
# print(age)

## Exercise
weight_lb = input('Weight in pounds: ')
weight_kg = round(0.45359237 * float(weight_lb), 2)
print('Weight in kilogram: ', weight_kg)
# Note: If expressions in print are connected by +, they must be in the same type.
#       Differnt type variables can be connected by comma ,