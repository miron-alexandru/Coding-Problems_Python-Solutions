class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            return ("*" * self.width + "\n") * self.height

    def get_amount_inside(self, shape):
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def __repr__(self):
        return "Square(side={})".format(self.side)

    def set_side(self, side):
        self.side = side
        super().set_width(side)
        super().set_height(side)

    def set_height(self, height):
        self.set_side(height)

    def set_width(self, width):
        self.set_side(width)
