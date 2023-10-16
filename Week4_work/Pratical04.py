# import math

# result = math.sqrt(2401)
# print (result)

# from math import log2

# result = log2(66)
# print (result)

msg = ("Hello There")


def displayTwice(msg):
    '''prints the passed in message twice'''
    print(msg)
    print(msg)


# displayTwice(msg)

# help(displayTwice(msg))


#a = 2
#b = 27


# def findMax(a,b):
# """Finds the maximum of two values."""
# if ( a > b ):
#    max = a
# else:
#      max = b

#   return max


# findMax(a,b)


#def multi(num1,num2):
 #   mul = num1 * num2
  #  return mul



#num1 = int(input("Enter a number:"))
#num2 = int(input("Enter a number:"))

#if num2 == " ":
 #   num2 = num1
  #  multi(num1,num2)
#else:
 #   multi(num1,num2)

#print ("sum:",multi(num1,num2))


#def someFunc(x, y, z):
#	print("x is", x, "\ny is", y, "\nz is", z)

#someFunc(y=2, z=3, x=1)

print ('Hello', 'There',sep='-')

#def calcAve(*numbers):
    #total = 0
    #for num in numbers:
   #     total += num
  #      return total/len(numbers)

# numbers = [2,27,9]
# num = input("enter a number:")


# print(calcAve(*numbers))

import math

hypot = lambda a,b : math.sqrt(a * a + b * b)

print (hypot(3,4))
print (type(hypot))

hours = input ("time in hours:")
minutes = input("time in minutes:")

a=hours
b=minutes

def myfunc(a,b):
    hours = lambda a: a * 3600
    minutes = lambda b: b * 60


print (myfunc(a,b))


