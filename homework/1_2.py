# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
#
# 100 -> 1 (1 + 0 + 0) |

num = int(input())

print((num//10**0)%10)

print(f"{(num//10**0)%10+(num//10**1)%10+(num//10**2)%10} ({(num//10**0)%10} + {(num//10**1)%10} + {(num//10**2)%10})")