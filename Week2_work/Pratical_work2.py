#total = 100

#total *= 4

#print('The total is', total)

#type(100 / 5)
#print(type)

#name = input('Hello what is your name?:')

#print("The length of you name is", len(name))

#age = int(input("Enter your age "))
#print("in one year your age will be", age + 1)

#num1 = int(input("enter a number:"))

#num2 = int(input("enter another number:"))

#sum = (num1 * num2)
#print(num1, "multiplied by", num2, "is", sum)


#print("this text includes characters such as '\' '"' and "'"\n \tthis is a new line that starts with a tab\n\t\t this line starts with two tabs ")
#print("\ " * 10,'\n', 'Hello There!', '\n', "\ " * 10 )

#print("This text spans three lines")
#print("and includes both single ('),")
#print("and double quotes(').")

#surname = "Palin"
#initial = surname[2]

#surname = "Palin"
#initial = surname[10]
#index out of range

#print (initial)

surname = ("Palin")
last = (surname[-2])
print(last)


middle =(surname[1:5])
print (middle)

tail = (surname[0:4])
print (tail)

lastThree = surname[:-3]

print (lastThree)

print(surname[0:1000000000]) #wouldnt cause an error

primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print (primes[0:4])

names = ["Tim", "Bill", "Graeme"]

names.append("joe")
print(names)

nums = [1,2,3] * 5

print (nums)