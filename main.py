from typing import List

triangle_matrix: List[List[float]] = [[-2, -1, 1, -2], [0, 3, -3, 0], [0, 0, 4, 4]]
var = triangle_matrix[2][len(triangle_matrix[2]) - 1] / triangle_matrix[2][len(triangle_matrix[2]) - 2]
print(var)
var_1 = (triangle_matrix[1][len(triangle_matrix[1]) - 1] - var * triangle_matrix[1][len(triangle_matrix[1]) - 2]) / \
        triangle_matrix[1][len(triangle_matrix[1]) - 3]
print(var_1)
vars = []
string_1 = []
print(vars)
vars.append(var)
for i in range(len(triangle_matrix[1]) - 2, 0, -1):
    triangle_matrix[1][i] = triangle_matrix[1][i] * vars[0]
print(triangle_matrix[1])
for i in range(len(triangle_matrix[1]) - 1):
    if triangle_matrix[1][i] != 0:
        string_1.append(triangle_matrix[1][i])
else:
    string_1.append(triangle_matrix[1][len(triangle_matrix[1]) - 1])
    string_1[1] = string_1[2] - string_1[1]
    del string_1[2]
var = string_1[1] / string_1[0]
vars.append(var)
print(vars)
print(string_1)
