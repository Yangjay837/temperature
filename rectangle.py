class Rectangle:
    def __init__(self, length, width):
        
        self.length = length
        self.width = width

    def compute_area_and_perimeter(self):
        area = self.length * self.width
        perimeter = 2 * (self.length + self.width)
        return area, perimeter


rect = Rectangle(4, 5)
area, perimeter = rect.compute_area_and_perimeter()
print(f"Area: {area}, Perimeter: {perimeter}")
      