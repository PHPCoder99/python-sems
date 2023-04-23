def checkNum(n, i = 2):
    if n == i:
        return True
    elif n % i == 0:
        return False
    elif i*i > n:
        return True
    return checkNum(n, i+1)


print(checkNum(5))