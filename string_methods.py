## String Methods
course = 'Python for Beginners'
print(len(course))  # len() here counts the number of characters in a string
# Here, print() and len() are general purpose functions. They don't belong to any objects like course.upper()

# lower() and upper() methods
print(course.upper())  # upper here is called a method. Here, convert all characters in course string to upper case
                           # Notice course.upper() returns a new string and keep original course string unchanged
print(course.lower())   # Convert all characters in course string to lower case
print(course)

# Key: Know the difference between functions and methods


## find() method
print(course.find('P'))    # course.find('P') returns the index of first appearance of 'P' in course string
print(course.find('o'))
print(course.find('O'))    # When the character 'O' is not in course string. course.find('O') returns -1
print(course.find('Beginners'))     # Returns the starting index of 'Beginners' in course string

print(course.replace('Beginners', 'Absolute Beginners'))    # course.replace('Beginners', 'Absolute Beginners') replace 'Beginners' with 'Absolute Beginners' in course string
print(course.replace('beginners', 'absolute beginners'))    # 'beginners' is not part of course string, hence the replacement can't be done
print(course.replace('n','k'))  # Replace all 'n' in course string to 'k'


# Check the existence of a string in course string
print('Python' in course)  # Returns a boolean to denote if 'Python' is included in course string

# Topics covered:
# len(0
# course.upper()
# course.lower()
# course.find()
# course.replace()
# '...' in course