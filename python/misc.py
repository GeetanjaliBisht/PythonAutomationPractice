users = [

    {"name":"John","age":25},

    {"name":"Alice","age":17},

    {"name":"Bob","age":35},

    {"name":"Emma","age":15}

]



def find_user(name):

    for user in users:

        if user["name"] == name:

            return user["name"]

    return False

    

print(find_user("Bob"))

print(find_user("John"))



elements_list = ["element1", "element2", "element3"]

empty_list = []

def print_element_count(elements):

    if len(elements) > 0:

        print(f"Found {len(elements)}")

    else:

        print("No elements found")



print_element_count(elements_list)

print_element_count(empty_list)



test_results = [

{"tc":"Login","status":"PASS"},



{"tc":"Logout","status":"FAIL"},



{"tc":"Search","status":"PASS"}

]

result_count = {}

for result in test_results:

    print(result["status"])

for result in test_results:

    if result["status"] in result_count:

        result_count[(result["status"])] += 1

    else:

        result_count[(result["status"])] = 1

        

print(result_count)



def is_login_successful(message):

    if message.casefold() == "Login Successful".casefold():

        return True

    

    return False



print(is_login_successful("login unsuccessful"))



caps = {

"platform":"Android",



"device":"Pixel 9",



"version":"15"



}



caps2 = {



"platform":"Android",

"version":"15"



}





def find_device(capabilities):

    if capabilities.get("device"):

        print(f"Running on {capabilities.get("device")}")

    else:

        print("Unknown Device")



find_device(caps)

find_device(caps2)



        