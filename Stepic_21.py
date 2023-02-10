#На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов
# в матрице. Далее вводятся сами элементы матрицы — слова, каждое на отдельной строке; подряд идут элементы сначала
# первой строки, затем второй, и т.д.
import numpy as np

n, m = int(input()), int(input())
matrix =[]
for i in range(n*m):
    matrix.append(input())
    if len(matrix) == m:
        print(*matrix)
        matrix.clear()
    print()
    if len(matrix) == n:
        print(*matrix)
        matrix.clear()



