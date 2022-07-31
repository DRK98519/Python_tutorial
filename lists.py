## Lists
# name = ['Saumya', 'Derek', 'Josh', 'George']
# print(name[1:3])  # Indexing for lists works the same as those in strings, use [] for indexing
# print(name[:])
# print(name)
#
# # Update a certain item in a list
# name[2] = 'Joshua'
# print(name) # By changing name[2], we updated the list name


## Exercise:
nums = [1, 123, 2345, 3456, 2]
max_num = nums[0]
for num in nums:
    if max_num < num:
        max_num = num
print(f'The largest number is {max_num}.')