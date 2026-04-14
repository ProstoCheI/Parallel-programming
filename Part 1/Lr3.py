def solve_bidiagonal(d, e, b, mode='lower'):
    """
    Резает СЛАУ Ax = b для двухдиагональной матрицы.

    :param d: Главная диагональ (длина n)
    :param e: Побочная диагональ (длина n-1)
    :param b: Вектор правой части (длина n)
    :param mode: 'lower' для нижней или 'upper' for верхней матрицы
    :return: Список с решением x
    """
    n = len(d)
    x = [0.0] * n

    if mode == 'lower':
        # Прямая подстановка
        x[0] = b[0] / d[0]
        for i in range(1, n):
            # e[i-1] соответствует элементу A[i, i-1]
            x[i] = (b[i] - e[i - 1] * x[i - 1]) / d[i]

    elif mode == 'upper':
        # Обратная подстановка
        x[n - 1] = b[n - 1] / d[n - 1]
        for i in range(n - 2, -1, -1):
            # e[i] соответствует элементу A[i, i+1]
            x[i] = (b[i] - e[i] * x[i + 1]) / d[i]

    return x


# --- ПРИМЕР ИСПОЛЬЗОВАНИЯ ---

# 1. Нижняя двухдиагональная матрица
# [ 2  0  0 ]   [x0]   [ 4 ]
# [ 1  3  0 ] * [x1] = [ 5 ]
# [ 0  2  4 ]   [x2]   [ 10]
diag_low = [2.0, 3.0, 4.0]
off_low = [1.0, 2.0]  # элементы под диагональю
b_low = [4.0, 5.0, 10.0]

sol_low = solve_bidiagonal(diag_low, off_low, b_low, mode='lower')
print(f"Решение (Lower): {sol_low}")

# 2. Верхняя двухдиагональная матрица
# [ 5  2  0 ]   [x0]   [ 7 ]
# [ 0  4  1 ] * [x1] = [ 9 ]
# [ 0  0  3 ]   [x2]   [ 6 ]
diag_up = [5.0, 4.0, 3.0]
off_up = [2.0, 1.0]  # элементы над диагональю
b_up = [7.0, 9.0, 6.0]

sol_up = solve_bidiagonal(diag_up, off_up, b_up, mode='upper')
print(f"Решение (Upper): {sol_up}")