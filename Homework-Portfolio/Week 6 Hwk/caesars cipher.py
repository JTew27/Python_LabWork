import random
#caesars cipher
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"



txt= str(input("enter a message:"))
key= int(input("enter a key between 1 and 25:"))
cipher= " "

if 0 < key <= 25:
    for i in txt:
        position=alphabet.find(i)
        newPosition = position + key
        cipher = cipher+alphabet[newPosition]
    print(cipher)
else:
    print("key invalid")

