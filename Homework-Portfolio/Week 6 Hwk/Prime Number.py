import math

def prime(num):
    if num < 2:
        print(num,"is not a prime number")
    i = 2
    while i*i <= num:
        if num % i ==0:
           return False
        i += 1
    print (num,"is a prime number")

num = int(input("Enter a number:"))

prime(num)