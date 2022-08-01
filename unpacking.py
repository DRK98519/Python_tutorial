## Unpacking
coord = (1, 2, 3)

x, y, z = coord # Unpack the tuple nums and assign its elements to x, y and z respectively
                # Same as the following:
                # x = coord[0]
                # y = coord[1]
                # z = coord[2]
print(f'x = {x}')
print(f'y = {y}')
print(f'z = {z}')
print(type(x))


## Unpacking also works for lists
coord = [1, 2, 3]
x1, y1, z1 = coord
print(f'''x1 = {x}
y1 = {y}
z1 = {z}
''')
print(type(x))