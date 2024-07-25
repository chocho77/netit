# In this example, Rectangle is the superclass, 
# and Square is the subclass.


class Rectangle:  
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * self.length + 2 * self.width
    

# Here we declare that the Square class inherits from the Rectangle class
class Square(Rectangle): 
    def __init__(self, length):
        super().__init__(length, length)

class Cube(Square):
    def surface_area(self):
        face_area = super().area()
        return face_area * 6

    def volume(self):
        face_area = super().area()
        return face_area * self.length

# main function
def main():
    print("Main func work.")
    square_one = Square(4)
    square_two = Square(5)
    
    square_area_one = square_one.area()
    square_area_two = square_two.area()

    cube = Cube(3)
    cube_surface_area = cube.surface_area()
    cube_volume = cube.volume()

    print(f"Square area : {square_area_one}")
    print(f"Square area : {square_area_two}")
    print(f"Cube surface area : {cube_surface_area}")
    print(f"Cube volume : {cube_volume}")


# driven code
if __name__ == '__main__':
    main()
    