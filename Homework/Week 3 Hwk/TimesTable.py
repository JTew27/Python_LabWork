num = int(input("Enter a number between 1 and 12:"))
count = 0

if num > 0 and num <=12:
    for n in range (13):
        print (count,"Multiplied by",num, ("="), num * count)
        count += 1

else:
    print ("Invalid Input")