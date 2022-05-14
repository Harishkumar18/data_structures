"""
Create a class called Shape. The constructor of this class should accept an argument called `dimension`
"""


class Shape:
    def __init__(self, dimension=None):
        self.dimension = dimension

    def get_value(self):
        return "shape"


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super(Rectangle, self).__init__()
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length*self.breadth


class square(Rectangle):
    def __init__(self, side):
        super(square, self).__init__(side, side)

    def get_value(self):
        return "square"


squ_obj = square(4)
print(squ_obj.get_value())




