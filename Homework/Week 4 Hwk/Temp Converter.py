
def choice():
    temp = int(input("Enter the temperature: "))
    ask = input("is that in Degrees Centigrade or Farenheit : c or f ?")
    ask.lower()
    if ask == "c":
        print(convertf(temp))
    elif ask == "f":
       print(convertc(temp))
    else:
        print("invalid input")
        choice()

def convertf(temp):
    f = (temp * 1.8)+32
    print ("That is ", f , "Degrees Farenheit")

def convertc(temp):
    c = (temp -32) * 5/9
    print ("That is", c , "Degrees Celsius")




choice()



