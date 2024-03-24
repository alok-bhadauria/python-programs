class Rectangle:
    def __init__(self) -> None:
        self.l = 0
        self.b = 0

    def setDetails(self, l, b):
        self.l = l
        self.b = b
    
    def area(self):
        return self.l * self.b
    
    def perimeter(self):
        return 2 * (self.l + self.b)

length = float(input("Enter length of rectangle : "))
breadth = float(input("Enter breadth of rectangle : "))
r1 = Rectangle()
r1.setDetails(length, breadth)
area = r1.area()
peri = r1.perimeter()
print(f"Area of rectangle with dimensions {length} and {breadth} is {area}")
print(f"Perimeter of rectangle with dimensions {length} and {breadth} is {peri}")