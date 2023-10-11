num = int(input("Enter a number:"))
count = 0


if num < 0:
    print ("negative")
    count =12
    for n in range(13):
        print(count, "Multiplied by", num, ("="), num * count)
        count -= 1

elif num >0:
    for n in range (13):
        print (count,"Multiplied by",num, ("="), num * count)
        count += 1

else:
    print ("Invalid Input")