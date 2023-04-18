scrabble = {
    "aeioulnstrавеинорст": 1,
    "dgдклмпу": 2,
    "bcmpбгёья": 3,
    "fhvwyйы": 4,
    "kжзхцч": 5,
    "jxшэю": 8,
    "qzфщъ": 10
}

text = input()
score = 0

for i in scrabble:
    for j in text:
        if j in i:
            score += scrabble[i]

print(score)
