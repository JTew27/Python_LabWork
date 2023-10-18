# Temp = [" "," "," "," "," "," "," "," "]
# = str(input("Enter the Temperature at 8am:"))

# for x in range(6):
#  temp = input("Enter the Temperature at this time of day:")
# temp.append(Temp)

eight_am = input("Enter the Temperature at 8am:")
ten_am = input("Enter the Temperature at 10am:")
twelve_pm = input("Enter the Temperature at 12am:")
two_pm = input("Enter the Temperature at 2pm:")
four_pm = input("Enter the Temperature at 4pm:")
six_pm = input("Enter the Temperature at 6pm:")
# changes to int from str in order for average to work as cant figure out how to convert it from string

temp8 = eight_am.replace('c','')
temp10 = ten_am.replace('c','')
temp12 = twelve_pm.replace('c','')
temp2 = two_pm.replace('c','')
temp4= four_pm.replace('c','')
temp6 = six_pm.replace('c','')
# eight_am.append(Temp)

Temp = [eight_am, ten_am, twelve_pm, two_pm, four_pm, six_pm]
#Temp = [temp8, temp10, temp12, temp2, temp4, temp6]
#print(Temp[:-1])

Temp.sort()
#print(Temp)
# Temp.sort(min,max)

highestTemp = (max(Temp))
print("HighestTemp: ", highestTemp,"C")

lowestTemp = (min(Temp))
print("LowestTemp: ", lowestTemp,"C")




#calc = (eight_am + ten_am + two_pm + four_pm + six_pm) / 6
calc = int(temp8 + temp10 + temp12 + temp2 + temp4 + temp6)/6
#doesnt work correctly logic error

#average = calc / 6
print("Average Temp: ", calc,"C")