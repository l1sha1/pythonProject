vars = [1 for i in range(len(matrix))]
for i in range(len(matrix) - 1, -1, -1):
    for k in range(len(matrix[i]) - 1):
        matrix[i][k] *= vars[k]
    for k in range(len(matrix[i]) - 2, i, -1):
        if i == len(matrix) - 1:
            break
        else:
            matrix[i][-1] -= matrix[i][k]
    vars[i] = matrix[i][-1] / matrix[i][i]
print(vars)
