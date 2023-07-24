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
# see . * + ^  $ ... meaning ($ - end of string) (^ meaning start with) (^[^@] enything expet @)
# ^[a-zA-Z0-9_] == ^\w    -> ^\W is the opposite of \w
if re.search(r"^\w+@[a-zA-Z0-9_]+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")