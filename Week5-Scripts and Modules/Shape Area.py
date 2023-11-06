from math import pi

def circ_area(r):
    Carea = (r*r)*pi
    print ("The area of a circle with the radius", r, "is",Carea)


def square_area(s):
    Sarea = (s*s)
    print ("The area of a sqaure with a side of", s, "is",Sarea )


def triangle_area(b,h):
    Tarea = ((b*h)/2)
    print ("The area of a triangle with a base of", b, "and a height of ",h,"is", Tarea )


def rect_area(side1,side2):
    Rarea = (side1 * side2)
    print ("The area of a rectangle with the sides", side1,"and",side2,"is", Rarea)





if __name__ == '__main__':
    shape = input("What shape would you like to find the area of:")

    if shape == "circle":
      r = int(input("Enter the radius of the shape:"))
      print(circ_area(r))

    if shape == "square":
      s = int(input("Enter one side of the square: "))
      print(square_area(s))

    if shape == "triangle":
      b = int(input("Enter the base of the triangle: "))
      h = int(input("Enter the height of the triangle: "))
      print(triangle_area(b,h))

    if shape == "rectangle":
      side1 = int(input("Enter a side of the rectangle: "))
      side2 = int(input("Enter another side of a rectangle: "))
      print(rect_area(side1,side2))





