n = int(input())

weight = int(input())
max_weight = weight
min_weight = weight

for _ in range(n-1):
    weight = int(input())
    if max_weight < weight:
        max_weight = weight
    if min_weight > weight:
        min_weight = weight

print(f"{min_weight} {max_weight}")
