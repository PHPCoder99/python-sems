array = input().split(", ")

k = int(input())

for _ in range(k):
    array.insert(0, array.pop())

print(*array)