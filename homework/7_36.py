def print_operation_table(operation, num_rows=6, num_cols=6):
    # пробел для красоты, искуственно добавляя символы к концу числа.
    return [[str(operation(i, j))+" "*(len(str(operation(num_rows, num_cols)))-len(str(operation(i, j)))) for j in range(1, num_cols+1)] for i in range(1, num_rows+1)]


table = print_operation_table(lambda x, y: x*y)

for i in range(6):
    print(*table[i])
