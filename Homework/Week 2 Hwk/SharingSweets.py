sweets = int(input("Enter the number of sweets:"))
pupils = int(input("Enter the number of pupils:"))

share = round(sweets/pupils)
rem = (sweets % pupils)

print ("The",pupils,"students each get",sweets,"sweets with", rem,"left over")