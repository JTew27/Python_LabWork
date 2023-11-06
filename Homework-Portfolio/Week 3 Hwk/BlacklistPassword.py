def passwordCheck():
    bad_passwords = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    password = input("Please enter a secure password:")
    ConfirmPass = input("Please confirm your password:")


    if len(password) > 8 and len(password) < 12:
        if password == ConfirmPass:
            if password != bad_passwords:
                print ("Password has been set")
    else:
        print ("Invalid password")
        passwordCheck()

passwordCheck()