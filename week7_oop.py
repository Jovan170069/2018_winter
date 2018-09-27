"""
Create a Shape class that comes with point length and width information
Plus a draw method.
"""
class Shape: # Creating a Shape class
    def __init__(self, length, width): #accepting the input arguments from caller
        self.length = length # setting the object's length
        self.width = width # setting the object's width
        #print("In the constructor of Shape. length = {}, width = {}".format(self.width, self.length))

    def draw(self):
        print("Drawing shape.")

    def __str__(self):
        return "length = {}; width = {}".format(self.length, self.width)

# Define a triangle class inherit from Shape
class Triangle(Shape): # Triangle inherits from Shape
    pass
    def draw(self):
        print("Drawing Triangle.")

shape1 = Shape(10, 20) # create an object base on the class Shape
print(shape1)
shape2 = Triangle(20, 15)
print(shape2.draw())
