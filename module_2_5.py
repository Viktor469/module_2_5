def get_matrix(n=2,m=2, value=10):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix
result = get_matrix(2, 2, )
print(result)