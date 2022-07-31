## Operator Precedence
x = 10 + 3 * 2  # Like in math, multiplication (division) apply first, then addition (subtractcion)
print(x)

# Operation order: exponentiation => multiplication (division) => addition (subtraction)

x = 10 + 3 * 2 ** 2 # This would return 22
print(x)

# Parenthesis raise precedence of certain operation like in math
x = (10 + 3) * 2 ** 2   # This would return 52
print(x)