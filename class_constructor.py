## Class Constructor
# Set instance attributes in class body instead of defining instance attributes to each particular instance
# Constructor get called whenever using the class to define a new object

class Point:
    def __init__(self, x, y):
        self.x = x  # x and y are attributes to current object in code whenever initialized.
        self.y = y
        # Self is a reference to the current object in the code

    def move(self, x_dist, y_dist):
        self.x += x_dist
        self.y += y_dist
        print(f"Move {x_dist} units in x direction and {y_dist} units in y direction")

    def draw(self):
        print("Draw")


point1 = Point(x=1, y=2)
print(type(point1))
print(f'({point1.x}, {point1.y})')
point1.move(2, 3)
print(f'({point1.x}, {point1.y})')


## Exercise:
class Person:
    def __init__(self, name):
        self.name = name    # name is an attribute to whatever objects in Person class
        # Methods and attributes are very different!!!

    def talk(self): # talk is a method of class Person
        print(f'{self.name} is talking.')


guest1 = Person('Derek')
guest1.talk()

guest2 = Person('Julianna')
guest2.talk()

