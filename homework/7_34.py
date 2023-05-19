poem = input().split()
has_rythm = [False if poem[i].count("аиуеоы") != poem[i-1].count("аиуеоы") else True for i in range(1, len(poem))][0]

print(has_rythm)
