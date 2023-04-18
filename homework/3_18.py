array = [1, 2, 4, 6, 1]
array.sort()
x = 3
result = 0
min_diff = abs(array[0]-x)

for i in range(len(array)):
    if abs(array[i]-x) < min_diff:
        min_diff = abs(array[i]-x)
        result = array[i]

print(result)
