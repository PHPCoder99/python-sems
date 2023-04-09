n = int(input())
max_warmth = 0
warmth_streak = 0

for _ in range(n):
    temp = int(input())
    if temp > 0:
        warmth_streak += 1

        if max_warmth < warmth_streak:
            max_warmth = warmth_streak
    else:
        warmth_streak = 0


print(max_warmth)
