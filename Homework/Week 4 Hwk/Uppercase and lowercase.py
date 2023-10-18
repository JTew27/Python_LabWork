str = str(input("Enter a phrase:"))

def check(str):
    upper = 0
    lower = 0
    for i in range(len(str)):
        if str[i].isupper():
            upper += 1
        elif str[i].islower():
            lower += 1
    print ("uppercase:",upper, "lowercase:",lower)

print(check(str))