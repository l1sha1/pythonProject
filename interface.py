from typing import List

import PySimpleGUI as sg
layout = [
    [sg.Text('Уравнение 1'), sg.Input(size=(20, 5)), sg.Input(size=(20, 5)), sg.Input(size=(20, 5))
     ],
    [sg.Text('Уравнение 2'), sg.Input(size=(20, 5)), sg.Input(size=(20, 5)), sg.Input(size=(20, 5)), sg.Button("Read")
     ],
    [sg.Text('Начальная матрица    '), sg.Output(size=(50, 5), key='0')],
    [sg.Text('Треугольная матрица  '), sg.Output(size=(50, 5))],
    [sg.Text('Результат            '), sg.Output(size=(50, 2))],
    [sg.Exit()]
]
window = sg.Window('Решение системы', layout)
while True:                             # The Event Loop
    event, values = window.read()
    v = []
    for i in values.values():
        v.append(float(i))
    v_1 = v[0:3]
    v_2 = v[3:6]
    matrix: List[List[float]] = [v_1, v_2]
    print("Начальная матрица")
    window['0'].update(matrix)

    # Задание матрицы - списки в списке с типом данных float
    def gauss(matrix):
        # Построение треугольной матрицы
        counter = 0
        while counter != len(matrix) - 1:  # количество циклов должно быть больше размерности матрицы - 1
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
    gauss(matrix)

    # print(event, values) #debug
    if event in 'Exit':
        break
