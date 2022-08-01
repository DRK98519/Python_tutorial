## Tuples
# Different from list, tuple can not changed, or immutable.

nums = [1, 2, 3]    # Define nums as a list with elements 1, 2, 3
nums = (1, 2, 3)    # Define nums as a tuple with elements 1, 2, 3
print(type(nums))

# There is no methods like nums.append(), nums.remove(), nums.insert(), nums.pop(), etc for nums as a tuple

## Tuple indexing
print(nums[0])
# nums[0] = 1     # This produces an error, since nums as tuple is immutable.