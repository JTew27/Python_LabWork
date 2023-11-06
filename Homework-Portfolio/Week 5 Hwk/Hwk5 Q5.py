import sys

program = sys.argv[0]

eight_am = sys.argv[1]
ten_am = sys.argv[2]
twelve_pm = sys.argv[3]
two_pm = sys.argv[4]
four_pm = sys.argv[5]
six_pm = sys.argv[6]
# changes to int from str in order for average to work as cant figure out how to convert it from string

temp8 = eight_am.replace('c','')
temp10 = ten_am.replace('c','')
temp12 = twelve_pm.replace('c','')
temp2 = two_pm.replace('c','')
temp4= four_pm.replace('c','')
temp6 = six_pm.replace('c','')

Temp = [eight_am, ten_am, twelve_pm, two_pm, four_pm, six_pm]
Temp.sort()


highestTemp = (max(Temp))
print("HighestTemp: ", highestTemp,"C")

lowestTemp = (min(Temp))
print("LowestTemp: ", lowestTemp,"C")

calc = int(temp8 + temp10 + temp12 + temp2 + temp4 + temp6)/6

print("Average Temp: ", calc,"C")