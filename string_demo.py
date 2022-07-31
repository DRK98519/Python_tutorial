## Python String Demo
course = "Python's Course for Beginners"    # Using "" to enclose strings allows us to use ' inside the string!
print(course)


course = 'Python for "Beginners'    # Similarly, using '' to enclose strings allows us to use " inside the string!
print(course)

# Multi-line string
course = '''
Hello Josh,

Here is our first email to you.

Thank you
The support team
'''    # Triple quotes ''' or """ allows us to print messages with multiple lines
print(course)


# String indexing
course = 'Python for Beginners'
print(course[0])    # Use [] to print particular characters in course string by indexing
print(course[-1])   # [-1] index refers to the last character in course string
print(course[-2])   # Negative index means index starting from the end of string
print(course[0:6])  # [0:6] index means that characters with index 0 to 5 will be printed and stops at index 6
print(course[0:])   # [0:] index refers to the characters in course string starting from index 0 to the end
print(course[:5])   # [:5] index refers to the characters in course string starting from beginning to index 4, and index 5 won't be printed
print(course[:])    # [:] index refers to all characters in course string

another = course
print(another)

## Exercise
name = 'Jennifer'
print(name[1:-1])   # This prints 'ennife' on screen