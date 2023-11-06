string = str(input("Enter a phrase:"))


def RCharacter(string):
    com = len(string)
    if com > 1 :
        print (string[:-1])
    else:
        print (string)

print(RCharacter(string))