## Return Commands
def square(x):  # Define a function called square with input parameter x and returns the value of x * x
    return x * x
    # x * x
    # If a UDF definition doesn't have return command, it would return object None by default.
    # None is an object that represents the absence of a value.

print(square(3))    # If square(3) is defined such that it returns nothing, this command would return void object None