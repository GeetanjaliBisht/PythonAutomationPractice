"""
Print only unique values after:

removing leading/trailing spaces
converting to lowercase 

Expected O/P:
[
    "login",
    "logout",
    "sign up",
    "profile"
]
"""

elements = [
    " Login ",
    "Logout",
    "LOGIN",
    "Sign Up",
    "login",
    " Profile "
]

Unique = []

for element in elements:
    if element.strip().lower() in Unique:
        continue
    else:
        Unique.append(element.strip().lower())

print(Unique)
