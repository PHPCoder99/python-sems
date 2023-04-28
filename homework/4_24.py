input_str = input()*2

if len(input_str) >= 3:
    max_sum = int(input_str[0])+int(input_str[1])+int(input_str[2])
    for i in range(len(input_str)-2):
        x = int(input_str[i])+int(input_str[i+1])+int(input_str[i+2])
        if x > max_sum:
            max_sum = x
    print(max_sum)
else:
    print("Invalid input.")
