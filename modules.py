## Modules
# Module is a file in Python with a lot of Python codes.
# A module is a file containing Python definitions and statements. The file name if the module name with the suffix
# .py appended. Module is good to organize the codes.


# def lbs_to_kg(weight):
#     return weight * 0.45
#
#
# def kg_to_lbs(weight):
#     return weight / 0.45


# Make the two UDFs above into a module, so that these functions can be used in other files just by importing the module
# to the program


# import converters    # Import entire converters module. Here, converters is an object
# print(round(converters.kg_to_lbs(95), 2))

from converters import kg_to_lbs    # Only import the UDF kg_to_lbs from converters module
from converters import lbs_to_kg
from nutils import find_max
import module1

module1.module_fx()
print(round(kg_to_lbs(95),2))       # Since we import a particular function in converters module, we can call the
                                    # function directly without prefixing the UDF call with object converters.
print(round(lbs_to_kg(205),2))

# Use modules to better organize the code. Instead of writing all codes in one file, we can organize the codes as
# (individually executable) modules in different files and import them as needed.

nums = [10, 3, 6, 2]
print(find_max(nums))