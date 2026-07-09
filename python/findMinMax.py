times = [12,14,22,10,18,25,9]

# find Average, Maximum, Minimum
max = times[0]
min = times[0]
sum = 0

for time in times:
    if time > max:
        max = time
    if time < min:
        min = time
    sum += time

print(f"Average: {sum/len(times)}")
print(f"Min: {min}")
print(f"Max: {max}")


#######################################
config = {
"platform":"Android",
"device":"Pixel",
"version":"15"
}

"""
Platform : Android
Device : Pixel
Version : 15
"""

def print_device_info(config):
    for key, value in config.items():
        print(f"{key}: {value}")

print_device_info(config)