"""
Return True only if password has:

minimum 8 characters
one uppercase
one lowercase
one digit

Otherwise return False.
"""

def validate_password(password):
    if len(password) > 7:
        if password != password.lower():
            if password != password.upper():
                if any(char.isdigit() for char in password):
                    return True
                else:
                    print("Password does not have digits")
            else:
                print("Password does not have lower case char")
        
        else:
            print("Password does not have upper case char")
    else:
        print("Password does not have enough characters")
    
    return False

print(validate_password("paSs0"))
print(validate_password("password"))
print(validate_password("Password"))
print(validate_password("Passw0rd"))

        

    