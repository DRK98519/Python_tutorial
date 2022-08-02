## Classes
# classes are used to define new types.
# Built-in types in Python: int, string, float, boolean, list, tuple, dict
# For complex objects, many of them can not be represented by Python built-in types, we can use classes to define the
# complex objects as new types.

nums = [1, 2, 3]

# Use class to define a type, point with methods like move, draw, get_distance, etc
# Pascal naming convention: When naming a new class, capitalize the first letter of every word in class name

# We defined a new type called Point. Using the new type Point, we can define new objects in the type Point. These objects
# are instances of the class Point.
# Class defines the templates of creating its objects. Objects are instances of this class.
class Point:
    # Define methods that belongs to the new type Point
    # Since there is no __init__ function in class methods. Hence, no arguments needed whenever using this class to
    # create a new object.
    def move(self):
        print("Move")   # The command move method conducts

    def draw(self):
        print("Draw")


print(type(Point()))
point1 = Point()
# Point().move()
point1.move()

# We can define attributes to a particular new object (instance attributes). The attributes only apply to the particular
# instance point1.
point1.x = 10
point1.y = 20

print(point1.x)
print(point1.y)