def summa(a, b):
    if b == 0:
        return a
    return summa(a+1, b-1)


print(summa(4, 5))