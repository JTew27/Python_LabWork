#unix grep
import sys

file = sys.argv[1]
string = sys.argv[2]

myFile = open(file, 'r')

fileD = myFile.readlines()

for line in myFile:
    if string in line:
        print(line)
    else:
        print("string does not appear")