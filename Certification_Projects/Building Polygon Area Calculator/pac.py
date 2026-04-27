
from math import sqrt
class Rectangle:

    def __init__ (self,width,height):
        self.width = width
        self.height = height


    def set_width(self,value):
        self.width = value


    def set_height(self,value):
        self.height = value


    def get_area(self):
        return self.width * self.height


    def get_perimeter(self):
        return 2 * (self.width + self.height)



    def get_diagonal(self):
        square_diagonal = self.width**2 + self.height**2
        return sqrt(square_diagonal)

    def get_picture(self):
        shape = ""
        if self.width > 50 or self.height >50:
            return "Too big for picture."
        else:
            for _ in range(self.height):
                shape += "*" * (self.width) + "\n"
            return shape



    def get_amount_inside(self,shape):
        Area = self.get_area()
        area = shape.get_area()

        return Area//area

    def __str__ (self):
        return f"Rectangle(width={self.width}, height={self.height})"



class Square(Rectangle):
  def __init__(self,side):
    super().__init__(side,side)

  def set_width(self, value):
    super().set_width(value)
    super().set_height(value)

  def set_height(self, value):
    super().set_height(value)
    super().set_width(value)

  def set_side(self,value):
    self.width = value
    self.height = value

  def __str__(self):
    return f"Square(side={self.width})"