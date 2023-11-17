#unix nl
#called from a textfile on the command line
import sys

file1 = sys.argv[1]# i enter a text file i already have made

file = open(file1, 'r')

lines = file.readlines()
count = 0

for line in lines:
    count += 1
    print("Line{}: {}".format(count, line.strip()))
