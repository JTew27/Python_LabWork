def circ_area(r):
    pass


def square_area(s):
    pass


def triangle_area(b,h):
    pass

def rect_area(side1,side2):
    pass





if __name__ == '__main__':
    shape = input("What shape would you like to find the area of:")

    if shape == "circle":
      r = int(input("Enter the radius of the shape:"))
      circ_area(r)

    if shape == "square":
      s = int(input("Enter one side of the square: "))
      square_area(s)

    if shape == "triangle":
      b = int(input("Enter the base of the triangle: "))
      h = int(input("Enter the height of the triangle: "))
      triangle_area(b,h)

    if shape == "rectangle":
      side1 = int(input("Enter a side of the rectangle: "))
      side2 = int(input("Enter another side of a rectangle: "))
      rect_area(side1,side2)





