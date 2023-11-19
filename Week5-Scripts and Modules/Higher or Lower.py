import random

number = random.randint(1,20)
count = 10

while count != 0:
    guess = int(input("Guess a number between 1 and 20:"))
    if guess == number:
        print("you guessed correctly")
        break
    else:
        count = count - 1
        print("incorrect you have",count,"attempts left")

if count == 0:
    print ("You Failed to Guess!")
    print ("The number was", number)