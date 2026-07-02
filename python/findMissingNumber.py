numbers = [1,2,3,4,5,7,8,9]

index = 1

for number in numbers:
    if number != index:
        print(index)
        break
    else:
        index += 1