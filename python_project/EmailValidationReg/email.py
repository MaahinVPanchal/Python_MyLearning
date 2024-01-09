import re

email_condition = r"^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

usr_email = input("Enter email: ")

# re.search,re.match
if re.match(email_condition, usr_email):
    print('Valid email')
else:
    print('Invalid email')
