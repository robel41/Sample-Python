""" Regular Expressions"""
import re
email = input("What is you email? ").strip()

"""if "@" in email and "." in email: # check if @ is in the email, w/out going through ech char
    print("Valid")
else:
    print("Invalid")"""
#############################

"""userName, domain = email.split("@")

if userName and "." in domain and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")"""

##############
#useing import re

if re.search(r"^.+@.+\.edu$", email):# see . * + ^  $ ... meaning ($ - end of string) (^ meaning start with)
        print("Valid")
else:
    print("Invalid")