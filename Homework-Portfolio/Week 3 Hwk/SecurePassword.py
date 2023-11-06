password = input("Please enter a secure password:")
ConfirmPass = input("Please confirm your password:")

if len(password) > 8 and len(password) < 12:
    if password == ConfirmPass:
        print ("Password has been set")

else:
    print ("Invalid password")