locators = {
    "login":"id_login",
    "password":"id_password",
    "submit":"id_submit"
}

"""
O/p: id_login if login found
or else "Locator not found"
"""
def get_locator(element_name):
    for elem, id in locators.items():
        if elem == element_name:
            return id
    return "Locator not found"

# Approach 2
locators = {
    "login":"id_login",
    "password":"id_password",
    "submit":"id_submit"
}

element_name = "login"
print(locators.get(element_name, "Locator not found"))
print(get_locator("login"))
print(get_locator("sign up"))
print(get_locator("submit"))

results = [
    "PASS",
    "FAIL",
    "PASS",
    "PASS",
    "FAIL",
    "PASS",
    "PASS",
    "FAIL"
]

"""
Passed : 5
Failed : 3
Pass Percentage : 62.5
"""
dict = {}
"""
for result in results:
    if result in dict:
        dict[result] += 1
    else:
        dict[result] = 1
"""
# alternate approach
for result in results:
    dict[result] = dict.get(result,0)+1

print(f"Passed: {dict["PASS"]}")
print(f"Failed: {dict["FAIL"]}")
print(f"Pass Percentage : {(dict["PASS"]/len(results))*100}")

