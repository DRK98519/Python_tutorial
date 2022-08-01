## Parameters (Functions with inputs)
def welcome_msg(first_name, last_name): # Define a function called welcome_msg with input variable called name.
    print(f'Hello, {first_name} {last_name}!')
    print('Welcome aboard!')
    # If the function is not called, the code in the function definition won't be compiled at all.

## Difference between parameters and arguments:
    # Parameter is the name of the variable that holds the input value inside the UDF. In welcome_msg, the parameter is name.
    # Argument is the actual input value used in every function call. For welcome_msg("Derek"), "Derek" is the argument.

print('Start')
welcome_msg("Derek", "Pan") # To call a function with input, you have to include a input when calling it.
welcome_msg("Julianna", "Yu") # Here, "Julianna" and "Yu" are positional arguments to welcome_msg.
                              # Argument correpondence to UDF parameters is determined by the argument position in UDF call.
print('Finish')
