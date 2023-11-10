unique = [" "]
message=str(input("Please enter a message :"))

dic={ "a":"i", "e":"o", "i":"u", "o":"a", "u":"e", "b":"m", "d":"t","g":"b","m":"d","t":"g","h":"c"}

encrypted = ""

for letter in message:
        if letter in dic:
                encrypted+=dic[letter]

        else:
                encrypted+=letter

print (encrypted)


for character in encrypted:
    if character not in unique:
        unique.append(character)

print ("The following letters appear:",unique)