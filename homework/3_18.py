array = [1, 2, 3, 3, 4, 6, 1]
x = 3
result = 0
min_diff = abs(array[0]-x)

for i in range(len(array)):
    if abs(array[i]-x) < min_diff:
        result = array[i]

print(result)
