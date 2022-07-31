## List Methods
nums = [1, 2, 4, 5, 63]
nums.append(20)     #nums.append(20) add 20 as a new element at the end to the nums lists, and updates nums to [1, 2, 4, 5, 63, 20]
print(nums)

nums.insert(3, 1) # nums.insert(3, 1) add 1 at index 3 in the original nums list, and updates nums to [1, 2, 4, 1, 5, 63, 20]
print(nums)

nums.remove(1)  # nums.remove(1) removes the first 1 in nums list, and updates nums to [2, 4, 1, 5, 63, 20]
print(nums)

print(nums.pop()) # By default, nums.pop() returns the last element in nums list and updates nums to [2, 4, 1, 5, 63]
print(nums)

nums.insert(0, 5)   # Updates nums to [5, 2, 4, 1, 5, 63]
print(nums.pop(3)) # nums.pop(5) returns the element at index 3 in nums lists, and updates nums to [5, 2, 4, 5, 63]
print(nums)

print(nums.index(5))    # nums.index(5) returns the index of first appearance of 5 in nums list, but doesn't change nums list
                        # If the number in nums.index(number) is not in nums list, then error occurs
print(nums)

print(50 in nums)   # We can also use logical operator in to check if 50 is included in nums lists, this returns boolean value True/False

print(nums.count(5))    # nums.count(5) returns the number of times 5 appears in nums list, doesn't change nums list

nums.sort()     # nums.sort() returns object None, but it reorders the nums list in ascending order, [2, 4, 5, 5, 63]
print(nums)

nums.reverse()  # nums.reverse() reverses the order nums lists is sorted, putting the original last element in nums to the first, vice versa
                # here it updates nums to [63, 5, 5, 4, 2]
print(nums)

nums2 = nums.copy() # nums.copy() copy the nums list to a new list nums2, any further changes in nums won't change nums2
print(nums2)

nums.clear()    #nums.clear() clears all elements in nums lists, and updates nums to []
print(nums)

print(nums2)



## Exercise:
# nums = nums2
nums = [2, 2, 4, 6, 3, 4, 5, 1]
unique_nums = []
for num in nums:
    if num not in unique_nums:
        # new_nums += [num]
        unique_nums.append(num)
print(unique_nums)
