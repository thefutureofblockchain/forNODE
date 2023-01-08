from validator_collection import validators, checkers, errors
a = input("enter: ")
is_email_address = checkers.is_email(a)
if is_email_address == True:
    print("Valid")
else:
    print("Invalid")
