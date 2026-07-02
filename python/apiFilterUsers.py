

def find_user(users, findUser):
    for user in users:
        if (user["name"]).casefold() == findUser.casefold():
            return user
    return False
# Print only Bob & John

users = [
    {"name":"John","age":25},
    {"name":"Alice","age":17},
    {"name":"Bob","age":30},
    {"name":"Emma","age":15}
]

details = find_user(users, "bob")
print(details["name"])
details = find_user(users, "john")
print(details["name"])
