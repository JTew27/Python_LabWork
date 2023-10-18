
def convertf(temp):
    ntemp = temp.replace('c','')
    print (ntemp)


    f = (float(ntemp) * 1.8)+32.0
    print ("That is ", f , "Degrees Farenheit")

temp = input("Enter the temperature: ")
convertf(temp)