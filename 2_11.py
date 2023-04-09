n = int(input())
a1 = 0
a2 = 1
i = 2

while a2 <= n:
    if a2 == n:
        print(i)
        break
    a1, a2 = a2, a1 + a2
    i += 1
    if a2 > n:
        print(-1)
        break
