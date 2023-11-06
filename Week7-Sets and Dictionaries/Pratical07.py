names = set(["John", "Eric", "Terry", "Michael", "Graham", "Terry"])

#print(names)

sentence = "this is a sentence conataining some letters"

#unique_letters = {x for x in sentence}

# remove whitespace
unique_letters = {x for x in sentence if x != " "}

#print(sentence)
#print(unique_letters)

#name = input("Enter your name:")

#if name not in names:
#   print("name is not found on the list")

staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}


managers = {"Kelly", "Jon", "Paul", "Sally", "Sue"}


# union operator: using | can add to the list of members
#staff = staff | {"Mark", "Ringo"}
staff = staff.union({"Mark", "Ringo"})
#print (staff)

#intersection opeterator: find common elements that appear in both lists using &
#staff_directors = staff & directors
staff_directors = staff.intersection()

#print(staff_directors)

#difference operator: using - to find elements that only appear in one set and not the other
#external = directors - staff
external = staff.difference()
#print(external)

#symmetric difference operator ^ to find elements in either set but not both
#staff_or_external = directors ^ staff
staff_or_external = staff.symmetric_difference(directors)
#print(staff_or_external)

vowels = set({"a", "e", "i"})
vowels.update({"u", "o"})
#print(vowels)

#if staff.issubset(managers):
 #   print("All Managers are staff members")

#if staff.issuperset(managers):
 #   print("All manager are staff members")

import math

roots = {n : math.sqrt(n) for n in range(9,15)}
print(roots)

for item in roots:
    print("The square root of",item, "is",roots.values() )


stock = {"apple":10, "banana":15, "orange":11}


#if "apple" in stock:
	#print("Apples are in stock")

#print("Apple stock level is", stock["apple"])

stock["pear"] = 50        	# add new key:value pair
stock["apple"] += 1        	# increase apple stock level

stock["kiwi"] = 10


#print(stock) #updated stock


# pop the "orange" returning its stock level
stock.pop("orange")

# update the stock to include two new fruits
stock.update(lemon=15, strawberry=99)

#print(stock)

stock.popitem()#removes item at the end of the list

#print(stock)

#for item in stock:
#	print(item)

#for item,level in stock.items():
	#print(item, "has a stock level of", level)
