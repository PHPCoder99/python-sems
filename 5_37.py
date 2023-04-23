def reverse(n):
    if n == 0:
        return ""
    i = input("Enter a number: ")
    return reverse(n-1) + i


print(reverse(5))