scrabble = {
    "aeioulnstr": 1,
    "dg": 2,
    "bcmp": 3,
    "fhvwy": 4,
    "k": 5,
    "jx": 8,
    "qz": 10,
    "авеинорст": 1,
    "дклмпу": 2,
    "бгёья": 3,
    "йы": 4,
    "жзхцч": 5,
    "шэю": 8,
    "фщъ": 10
}

text = input()
score = 0

for i in scrabble:
    for j in text:
        if j in i:
            score += scrabble[i]

print(score)
