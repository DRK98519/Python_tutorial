## Project: Weight Converter
weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
# if (unit == 'L') or (unit == 'l'):
    print(f'Weight (lb): {weight}')
    print(f'Converted weight (kg): {round(0.45359237 * float(weight), 2)}')
elif unit.upper() == 'K':
# elif (unit == 'K' or unit == 'k'):
    print(f'Weight (kg): {weight}')
    print(f'Converted weight (lb): {round(2.20462262 * float(weight), 2)}')
else:
    print('Unit is unacceptable.')
