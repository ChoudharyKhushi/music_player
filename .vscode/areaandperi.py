class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
rect = Rectangle(length, breadth)
print(f"Area of the rectangle is {rect.area():.2f}")
print(f"Perimeter of the rectangle is {rect.perimeter():.2f}")