## Dictionary (dict data type)
# Dictionary stores information that comes as key value pairs. Dictionary can store values with any type. The key is usually string.

customer = {
    "name": "John Smith",
    "age": 30,
    # "age": 40,  # A dictionary doesn't encourage duplicate value assignments to the same key
    "is_verified": True
}

print(type(customer))
print(customer["name"]) # Print the value associated with the key "name" in customer dictionary
# print(customer["birthday"]) # Error occurs since "birthday" is not a key in customer dictionary

# The key in dict variable is case sensitive.
print(customer.get("birthday")) # This won't show error even if "birthday" is not a key in customer dict
print(customer.get("birthday", "May 19 1998"))  # customer.get("birthday", "May 19 1998") returns default value "May 19 1998", if "birthday" is not a key in customer dict

customer["birthday"] = 'Jan 6 1998' # Update a dict with a new key and value
print(customer)
print(customer.get("name")) # customer.get("name") returns the value assigned to key "name"



## Exercise:
num_2_text = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}
msg = ''
phone_num = input('Phone: ')
for num in phone_num:
    msg += num_2_text.get(num, '*') + ' '
    # msg += num_2_text[num] + ' '
print(msg)