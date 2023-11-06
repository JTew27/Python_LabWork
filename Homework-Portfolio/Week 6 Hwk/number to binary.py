def binary(decimal):
    if (decimal > 0):
        binary((int)(decimal / 2))
        print(decimal % 2, end='')


decimal = int(input("Enter a decimal number:"))
binary(decimal)