from math import sqrt

s = int(input())
p = int(input())

if s**2-4*p < 0:
    print("No real-valued solutions exist")
else:
    y = int((s+sqrt(s**2-4*p))/2)
    print(s-y, y)
