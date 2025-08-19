class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(
            f"{self.name} has an area of {self.area} and perimeter of {self.perimeter}"
        )


class Square(Shape):
    """
    A class representing a square, derived from the Shape class.
    """

    def __init__(self, side: int):
        """
        Initializes the Square object.

        Args:
            side (int): The length of the square's side.
        """
        # Call the constructor of the base class (Shape) and set the name.
        super().__init__("Square")

        # Assign the side to the attribute of this class.
        self.side = side

        # Call the methods to compute and set the area and perimeter.
        self.compute_area()
        self.compute_perimeter()

    def compute_area(self):
        """
        Computes the area of the square (side * side) and assigns it
        to the 'area' attribute inherited from the Shape class.
        """
        self.area = self.side * self.side

    def compute_perimeter(self):
        """
        Computes the perimeter of the square (4 * side) and assigns it
        to the 'perimeter' attribute inherited from the Shape class.
        """
        self.perimeter = 4 * self.side
