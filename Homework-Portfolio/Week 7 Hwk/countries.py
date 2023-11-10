import random
dict1 ={"england":"london","france":"paris","italy":"rome"}
list1=[key for key in dict1.keys()]

print (list1)

def countries(dict1,list1):
    user = input("Enter a country: ")
    country = user.lower()
    if country in dict1:
        print("The Capital of", user, "is", dict1.get(country))
        countries(dict1, list1)
    else:
        print("This country does not appear in our list,", "\n", )
        capital = input("Enter the capital of this new country:")
        dict1.update({country:capital})
        print(dict1)
        countries(dict1, list1)



countries(dict1,list1)