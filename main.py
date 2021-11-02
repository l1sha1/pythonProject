import sys


def gauss(matrix):
# Построение треугольной матрицы
    counter = 0
    while counter != len(matrix) - 1: # количество циклов должно быть больше размерности матрицы - 1
        print(counter, "номер цикла")
        """Цикл пробегает по строкам, делая первый ненулевой коэффициент равным 1"""
        for i in range(counter, len(matrix)):
            if matrix[i][counter] != 0:
                p = matrix[i][counter]
            elif matrix[i][counter] == 1.0:
                p = matrix[i][counter]
            else:
                p = matrix[i][counter + 1]
            for j in range(len(matrix[i])):
                matrix[i][j] = matrix[i][j] / p
            print(i)
            print(*matrix, sep='\n')
        """Цикл пробегает по строкам, записывая в строку значения после вычитания из этой строки предыдущей"""
        for i in range(len(matrix) - 1, counter, -1):
            if matrix[i][counter] == 0:
                continue
            else:
                for k in range(len(matrix[i])):
                    matrix[i][k] = matrix[i][k] - matrix[i - 1][k]
        counter += 1
        print()
        print(*matrix, sep='\n')
"""Проверка, есть ли корни у системы"""
    for g in range(len(matrix)):
        counter_null = 0
        for j in range(len(matrix[g]) - 1):
            if matrix[g][j] != 0:
                continue
            else:
                counter_null += 1
        if counter_null == len(matrix[g]) - 1:
            print("Решений нет")
            sys.exit()
    # Расчет корней
    """Задаем вектор неизвестных, состоящий из числа 1, равного количеству неизвестных"""
    vars = [1 for i in range(len(matrix))]
    for i in range(len(matrix) - 1, -1, -1):
        for k in range(len(matrix[i]) - 1):
            matrix[i][k] *= vars[k]
        for k in range(len(matrix[i]) - 2, i, -1):
            if i == len(matrix) - 1:
                break
            else:
                matrix[i][-1] -= matrix[i][k]
        vars[i] = round((matrix[i][-1] / matrix[i][i]) * 100) / 100
    print(vars)


n = int(input("Введите количество уравнений "))

matrix_new = []
for i in range(n):
    matrix_element = input("Введите коэффициенты уравнения (через пробел) ").split(' ')
    matrix_element_list = []
    for k in range(len(matrix_element)):
        if matrix_element[k] ==' ':
            continue
        else:
            matrix_element_list.append(float(matrix_element[k]))
    matrix_new.append(matrix_element_list)
matrix_new = sorted(matrix_new, key=lambda matrix_new: abs(matrix_new[0]), reverse=True)
gauss(matrix_new)

