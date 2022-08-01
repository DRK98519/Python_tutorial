## Functions (UDF, user defined function)
## Always define function before its function call
def welcome_msg(): # def refers to definition of a function. Here, function is named with welcome_msg. Function requires no inputs.
    print('Hello!')
    print('Welcome aboard!')
    # If the function is not called, the code in the function definition won't be compiled at all.


# Compiler starts execution here.
print("Start")
welcome_msg()   # Function call of welcome_msg
print("Finish")