array = [0, -1, 5, 2, 3]
streak = 0

for i in range(1, len(array)):
    if array[i] > array[i-1]:
        streak += 1

print(streak)
