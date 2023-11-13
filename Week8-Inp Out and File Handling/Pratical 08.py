from math import pi
width = 10
height = 5.3

sum = (width*height)

print(f"A rectangle with a width of {width} and a height of {height} is {sum:.3f}")

name = "James"

age = 18


print(f"{name:15} - {age:10}")
print(f"{name:>15} - {age:10}")
print(f"{name:^15} - {age:^10}")
print(f"{name:@^15} - {age:#^10}")

print(f"{name:$^20} - {age:$^20.2f}")

r = 3
area = ((r*r)*pi)
print(f"The area of a circle with a radius{r:^5}has an area of {area:<5}".format(r,area))

str = "My name is {fname} and i am {age}".format(fname = "James", age = 18)
print(str.format(age=18))


#f = open("info.txt")



#for line in f:
  #  print(line)
#f.close()

f = open("f1.txt")

#f.write("I have written this into the file")


#contents = f.read()
#print (contents)

#f.close()

# open new file for writing
#f1 = open("nextfile.txt", "w")
# open existing file for appending
#f2 = open("file123.txt", "a")
# open file for for reading and writing
#f3 = open("fileABC.txt", "r+")
# open file for reading in binary mode
#f4 = open("image.png", "rb")

#with open("info.txt") as f:
   # lines = f.readlines()
   # print(lines)

#value = 10.768572
#print(f"Value is {value * 10}")
#print(f"Value is {value:16.2f}")
#print(f"Value is {value:0>16.2f}")
for next in f:
    print(next)
print("Length = {1} Width = {0}".format(10,20))

print("Hello".rjust(10))

#for x in range(10):
 #   str = "#"
  #  str.rjust(x)
   # x += 1
    #print(str)

for n in range(10,0,-1):
    line = "#" * n
    line.rjust(n)
    print(line)

f.seek(0)