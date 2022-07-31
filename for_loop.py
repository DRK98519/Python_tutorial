## For loop
# for item in 'Python':   # In each iteration, item would be one character in the sting 'Python' starting with 'P'
#     print(item)
#
#
# # In Python, we can define a list by []. A list can combine data with different types as a vector to a new variable
#
# for item in ['John', 'Derek', 'Allen']: # This for loop iterates over each string in the list
#     print(item)


# for item in range(10): # range(10) refers to the numbers 0 1 2 3 4 5 6 7 8 9, stops at 10 and 10 is not included
#                        # range(5, 10) refers to the numbers 5 6 7 8 9
#                        # range(5, 10, 2) refers to the numbers 5 7 9, with increment of 2
#     print(item)


## Exercise:
price = [10, 20, 30]
tot_cost = 0
for cost in price:
    tot_cost += cost
print(f'Total Cost: ${tot_cost}')
