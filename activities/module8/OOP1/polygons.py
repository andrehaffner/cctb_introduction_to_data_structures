
class Rectangle:
    def __init__(self):
        self.length = float(input("Rectangle length: "))
        self.width = float(input("Rectangle width: "))

    def perimeter(self): return self.length*2 + self.width*2

    def area(self): return self.length*self.width

    def display(self):
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())

