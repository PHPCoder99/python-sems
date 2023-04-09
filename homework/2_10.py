n = int(input())
heads_count = 0
for i in range(n):
    heads_count += int(input())
print(min(heads_count, n-heads_count))
