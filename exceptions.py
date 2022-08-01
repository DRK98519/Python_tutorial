## Exceptions (Topics on error message)
# When a program terminates, terminal shows "Process finished with exit code 0" means that the program terminate without any error.
# "Process finished with exit code (non-zero number)" means the program crashes.
# The type of error is usually displayed in terminal after running the program.


# age = int(input('Age: '))
# print(age)
# # If age is a strong, the program would crash.


try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:  # Following block of code activates when program encounters a ValueError
    print('Invalid value')  # New error message for a ValueError encounter instead of crashing the program
except ZeroDivisionError:
    print("Can't divide by 0")  # New error message for ZeroDivisionError instead of crashing the program
