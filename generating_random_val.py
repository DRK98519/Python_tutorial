## Use Python built-in modules to generate random values
import random
print(random.__file__) # Shows the directory Python built-in package random is located in

for i in range(3):
    print(random.random())  # random.random() generates a random number between 0 and 1


for i in range(3):
    print(random.randint(10, 20))   # random.randint(10,20) generates a random integer between 10 and 20


members = ["Derek", "Julianna", "Francesca", "Kelvin", "Stella"]
print(random.choice(members))   # random.choice(members) randomly choose an element in the members list