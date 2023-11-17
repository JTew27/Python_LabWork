#unix diff
import sys

filet1 = sys.argv[1]
filet2 = sys.argv[2]

file1 = open(filet1, 'r')

file2 = open(filet2, 'r')

f1data = file1.readlines()
f2data = file2.readlines()

i = 0

for line1 in f1data:
    i += 1

    for line2 in f2data:

        if line1 == line2:
            print(i,": Same")
        else:
            print(i,":")
            print("\tFile 1:",line1, end='')
            print("\tFile 2:",line2, end='')
        break

file1.close()
file2.close()



