from typing import List

import PySimpleGUI as sg
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
        [sg.Text('Треугольная матрица'), sg.Output(size=(50, 5))],
        [sg.Text('Результат             '), sg.Output(size=(50, 2))],
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
        for k in range(n):
            left = k * (n + 1)
            right = len(v) / n + 1 + k * (n + 1)
            row = v[left:right]
            matrix.append(row)
        print(left, right, matrix)

        if event in 'Exit':
            break
