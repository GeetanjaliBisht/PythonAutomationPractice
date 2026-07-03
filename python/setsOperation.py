numbers = [1,2,2,3,4,4,5]

unique = set(numbers)
print(unique)

a = {1,2,3,4}

b = {3,4,5,6}

print(a & b) # find common bw a & b
print (a | b) # find all unique values in a & b
print(a - b) # find values unique to a