from typing import List

import PySimpleGUI as sg
sg.theme('DarkAmber')
demension = [
    [sg.Text('Введите размерность системы'), sg.Input(size=(20, 5), key='n'), sg.Button('OK')
     ]
]
dem_num = sg.Window('Размерность системы', demension)
while True:                             # The Event Loop
    event, values = dem_num.read()
    for i in values.values():
        n = int(i)
    dem_num.close()

    equals = []
    for i in range(n):
        coeff = [sg.Input(size=(20, 5)) for _ in range(n + 1)]
        equals.append([sg.Text('Уравнение')])
        equals[i] += coeff
    layout = [
        *equals,
        [sg.Button('Read')],
        [sg.Text('Треугольная матрица'), sg.Output(size=(50, 5), key="Triangle")],
        [sg.Text('Результат'), sg.Output(size=(50, 5), key="Res")],
        [sg.Exit()]
        ]
    window = sg.Window('Решение системы', layout)
    while True:  # The Event Loop
        event, values = window.read()
        v = []
        matrix: List[List[float]] = []
        for i in values.values():
            v.append(float(i))
        print(v)
        for k in range(1, n + 1):
            row = v[(k - 1) * (n + 1):(n + 1) * k]
            matrix.append(row)
        print(*matrix, sep="\n")
        # Задание матрицы - списки в списке с типом данных float

        import sys

        def gauss(matrix):
            # Построение треугольной матрицы
            counter = 0
            while counter != len(matrix) - 1:  # количество циклов должно быть больше размерности матрицы - 1
                """Цикл пробегает по строкам, делая первый ненулевой коэффициент равным 1"""
                for i in range(counter, len(matrix)):
                    if matrix[i][counter] != 0:
                        p = matrix[i][counter]
                    elif matrix[i][counter] == 1.0:
                        p = matrix[i][counter]
                    else:
                        p = matrix[i][counter + 1]
                    try:
                        for j in range(len(matrix[i])):
                            matrix[i][j] = matrix[i][j] / p
                    except ZeroDivisionError:
                        zeros = 0
                        for j in range(len(matrix[i])):
                            if matrix[i][j] == 0:
                                zeros += 1
                            else:
                                break
                        if zeros == len(matrix[i]) - 2:
                            p = matrix[i][-2]
                        else:
                            p = matrix[i][len(matrix[i]) - zeros]
                        for j in range(len(matrix[i])):
                            matrix[i][j] = matrix[i][j] / p

                    """Цикл пробегает по строкам, записывая в строку значения после вычитания из этой строки предыдущей"""
                for i in range(len(matrix) - 1, counter, -1):
                    zeros = 0
                    for j in range(len(matrix[i])):
                        if matrix[i][j] == 0:
                            zeros += 1
                        else:
                            break
                    if zeros >= counter + 1:
                        continue
                    else:
                        for k in range(len(matrix[i])):
                            matrix[i][k] = matrix[i][k] - matrix[i - 1][k]
                counter += 1
            window["Triangle"].update(list(matrix))
            #  print(*matrix, sep='\n')

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
            try:
                vars = [1 for _ in range(len(matrix))]
                for i in range(len(matrix) - 1, -1, -1):
                    for k in range(len(matrix[i]) - 1):
                        matrix[i][k] *= vars[k]
                    for k in range(len(matrix[i]) - 2, i, -1):
                        if i == len(matrix) - 1:
                            break
                        else:
                            matrix[i][-1] -= matrix[i][k]
                    vars[i] = round((matrix[i][-1] / matrix[i][i]) * 100) / 100
                window["Res"].update(vars)
                #print(*vars)
            except ZeroDivisionError:
                print("Проверьте введенную систему уравнений")
        gauss(matrix)

        if event in 'Exit':
            break
