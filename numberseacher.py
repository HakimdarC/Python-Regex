import re

def PhoneNumberSeacher(text):
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.findall(message)

    for num in mo:
        print('Phone number found: ' + num)
        

message = input("Enter message: ")
PhoneNumberSeacher(message)




