## Formatted String
first_name = 'John'
last_name = 'Smith'

# Print John [Smith] is a coder.
message = first_name + ' [' + last_name + '] is a coder.'   # Not ideal, since it gets messy easily
print(message)

msg = f'{first_name} [{last_name}] is a coder.' # This is a formatted string, much cleaner
print(msg)