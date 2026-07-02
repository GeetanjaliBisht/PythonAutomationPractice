numbers = [2, 5, 3, 8, 2, 7, 5, 9, 2]

dict = {}

for number in numbers:
    if number in dict:
        dict[number] += 1
    else:
        dict[number] = 1

list = []
for number in dict:
    if dict[number] > 1:
        list += [number]
print(list)