## 2D Lists (This is like the built-in matrix in Python. Of course, we can use numpy package for more advanced use)
# 2D List is a list of lists, where each element in the 2D list is another list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(matrix)   # Print the entire matrix 2D list
print(matrix[0]) # Print the first list in matrix 2D list, print [1, 2, 3]
print(matrix[0][0]) # Print the first element in the first list in matrix 2D list, print 1

# Update a 2D List
matrix[1][2] = 60
print(matrix)

# iterations in 2D List
for row in matrix: # Since matrix here is a 2D list, row would be its elementary list in every iteration. eg. row = [1, 2, 3]
    for num in row:
        print(num)