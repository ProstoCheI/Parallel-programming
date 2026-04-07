def invert_bidiagonal(d, e, mode='lower'):
    """
    Вычисляет обратную матрицу для двухдиагональной матрицы.

    :param d: Главная диагональ (длина n)
    :param e: Побочная диагональ (длина n-1)
    :param mode: 'lower' (нижняя) или 'upper' (верхняя)
    :return: Двумерный список (матрица n x n)
    """
    n = len(d)
    # Инициализируем пустую матрицу n x n нулями
    res = [[0.0 for _ in range(n)] for _ in range(n)]

    if mode == 'lower':
        for j in range(n):
            # Заполняем столбец j, начиная с диагонали вниз
            res[j][j] = 1.0 / d[j]
            for i in range(j + 1, n):
                # Формула: B[i,j] = - (e[i-1] * B[i-1,j]) / d[i]
                res[i][j] = -(e[i - 1] * res[i - 1][j]) / d[i]

    elif mode == 'upper':
        for j in range(n):
            # Заполняем столбец j, начиная с диагонали вверх
            res[j][j] = 1.0 / d[j]
            for i in range(j - 1, -1, -1):
                # Формула: B[i,j] = - (e[i] * B[i+1,j]) / d[i]
                res[i][j] = -(e[i] * res[i + 1][j]) / d[i]

    return res


def print_matrix(matrix):
    for row in matrix:
        print([round(x, 4) for x in row])


# --- ПРИМЕР ---

# Нижняя двухдиагональная матрица:
# [ 2  0  0 ]
# [ 1  3  0 ]
# [ 0  2  4 ]
d_val = [2.0, 3.0, 4.0]
e_val = [1.0, 2.0]

print("Обратная матрица (Lower):")
inv_low = invert_bidiagonal(d_val, e_val, mode='lower')
print_matrix(inv_low)

# Проверка: если умножить inv_low на исходный вектор b=[4, 5, 10],
# мы должны получить x=[2, 1, 2] из предыдущего примера.