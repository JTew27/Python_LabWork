group1 = int(input("Enter the number of students:"))
groupSize = int(input("Enter the size of each group:"))

split = round(group1/groupSize)
rem= (group1 % groupSize)
print ("There is",split, "groups of students with a small group of", rem)
print("\n")