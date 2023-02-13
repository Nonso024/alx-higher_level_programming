#!/usr/bin/python3
""" Module represents a class that represnts rectangle """


from models.base import Base


class Rectangle(Base):
    """ A rectangle class that inherits from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes attributes of the class """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # List of getter functions
    def width(self):
        """ Gets value of width """

        return self.__width

    def height(self):
        """ Gets value of height """

        return self.__height

    def x(self):
        """ Gets value of x """

        return self.__x

    def y(self):
        """ Gets value of y """

        return self.__y

    # List of setter functions
    @width.setter
    def width(self, value):
        """ sets width """

        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """ sets the height """

        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """ sets x """

        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """ sets y """

        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >=0")

        self.__y = value

    def area(self):
        """ This function returns the area of a rectangle """

        return (self.__height * self.__width)

    def display(self):
        """ Displays the rectangle using # """

        for y in range(self.y):
            print("")
        for row in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ defines a format for the string representation of the class """

        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
         """ updates the attribute of the rectangle """

        attr = ["id", "width", "height", "x", "y"]

        if not args:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)
        else:
            i = 0
            for arg in args:
                setattr(self, attr[i], arg)
                i += 1
                if i > 4:
                    break

    def to_dictionary(self):
        """ returns the dictionary representation """

        attrs = ["id", "width", "height", "x", "y"]
        dict_rep = {}

        for attr in attrs:
            val = getattr(self, attr)
            dict_rep[attr] = val

        return dict_rep
