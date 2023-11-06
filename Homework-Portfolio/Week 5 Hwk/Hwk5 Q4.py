import validators
import sys

valid = validators.url(sys.argv[1])

if valid==True:
    print("Url is valid")
else:
    print("Invalid url")