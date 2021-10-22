from typing import List

matrix: List[List[float]] = [[1, 2, -4, 3], [2, -3, 3, -1], [3, 2, -2, 5]] # Задание матрицы - списки в списке с типом данных float
# Построение треугольной матрицы
counter = 0
while counter != len(matrix) - 1: # количество циклов должно быть больше размерности матрицы - 1
    print(counter, "номер цикла")
    """Цикл пробегает по строкам, делая первый ненулевой коэффициент равным 1""""
    for i in range(counter, len(matrix)):
        if matrix[i][counter] != 0:
            p = matrix[i][counter]
        elif matrix[i][counter] == 1:
            p = matrix[i][counter]
        else:
            p = matrix[i][counter + 1]
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j] / p
        print(i)
        print(*matrix, sep='\n')
    """Цикл пробегает по строкам, записывая в строку значения после вычитания из этой строки предыдущей"""
    for i in range(len(matrix) - 1, counter, -1):
        for k in range(len(matrix[i])):
            matrix[i][k] = matrix[i][k] - matrix[i - 1][k]
    counter += 1
    print()
    print(*matrix, sep='\n')
# Расчет корней
"""Задаем вектор неизвестных, состоящий из числа 1, равного количеству неизвестных"""
vars = [1 for i in range(len(matrix))]
""""""
for i in range(len(matrix) - 1, -1, -1):
    for k in range(len(matrix[i]) - 1):
        matrix[i][k] *= vars[k]
    for k in range(len(matrix[i]) - 2, i, -1):
        if i == len(matrix) - 1:
            break
        else:
            matrix[i][-1] -= matrix[i][k]
    vars[i] = round(matrix[i][-1] / matrix[i][i])
print(vars)
