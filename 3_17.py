array = input().split(", ")
array2 = []

for i in array:
    if i not in array2:
        array2.append(i)

print(len(array2))