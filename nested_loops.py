## Nested Loops

# for x in range(4):
#     for y in range(4):
#         print(f'({x}, {y})')

## Exercise
nums = [2, 2, 2, 2, 5]
for num in nums:
    msg = ''
    for iter in range(num):
        msg += 'x'
    print(msg)