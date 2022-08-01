## Keyword Arguments
# Positional argument: Aruguments to UDF call that determines its correspondence to UDF parameters by its position (order of input vs. order of parameter in UDF def)
# Keyword argument: Arguments whose positions in UDF call won't affect its correspondence in UDF parameters

# Example of Keyword Arugment:
def welcome_msg(first_name, last_name): # Define a function called welcome_msg with input variable called name.
    print(f'Hello, {first_name} {last_name}!')
    print('Welcome aboard!')

# Advantage of Positional Arguments: They increase the readability of the code when calling the function.
print("Start")
welcome_msg(last_name="Pan", first_name="Derek")
print('Finish')

# Usually, using positional arguments in UDF call is enough. But you still need keyword arguments sometimes.
## NOTE: If you want to mix keyword arguments and positional arguments together in a UDF call,
       # all the positional arguments must go before all keyword arguments.