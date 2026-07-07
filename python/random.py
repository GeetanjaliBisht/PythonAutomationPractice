numbers = [10, 15, 20, 25, 30]

# Print only numbers divisible by 10

for number in numbers:
    if number % 10 == 0:
        print(number)
        
text = "Playwright"
# Count vowels
count = 0
for chr in text:
    if chr in "AEIOUaeiou":
        count += 1
        # print(chr)

print(count)

users = [
    {"name":"John","active":True},
    {"name":"Alice","active":False},
    {"name":"Bob","active":True}
]

# Print only active users
for user in users:
    if user["active"] == True:
        print(user["name"])

