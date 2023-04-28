string = "a a a b c a a d c d d".split()

for i in range(len(string)):
    print(f"{string[i]}_{string[0:i].count(string[i])}" if string[0:i].count(string[i]) != 0 else string[i], end=" ")

b =[]

b.append(i[0:2])