## Inheritance
# class Dog:
#     def walk(self):
#         print("Walk")
#
#
# class Cat:
#     def walk(self):
#         print("Walk")


# This is bad programming above. DRY (Don't Repeat Yourself). This programming habit causes trouble when debugging.
# Use inheritance to avoid repetition in class definitions


class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):# Dog(Mammal) indicates that the class Dog inherits methods and attributes from its parent class Mammal
    def bark(self): # Python doesn't like empty class. Either add some methods or attributes specific to the child class
        print('Bark')   # Dog, or use pass command to indicate no specific methods or attributes to Dog class


class Cat(Mammal):
    def be_annoying(self):
        print('Be annoying')


pet1 = Dog()
pet1.walk()
pet1.bark() # pet1.bark() is a method particularly defined for child type Dog()

pet2 = Cat()
pet2.walk()
pet2.be_annoying()