def solve_upper_bidiagonal(d, u, b):
    """
    Решает СЛАУ Ax = b для верхней двухдиагональной матрицы.

    :param d: Список элементов главной диагонали [d_0, d_1, ..., d_{n-1}]
    :param u: Список элементов верхней диагонали [u_0, u_1, ..., u_{n-2}]
    :param b: Список свободных членов [b_0, b_1, ..., b_{n-1}]
    :return: Список решений x
    """
    n = len(d)
    # Создаем список для ответов такой же длины, как b
    x = [0] * n

    # 1. Находим последний элемент (база обратной подстановки)
    # Проверка на ноль, чтобы не поймать ZeroDivisionError
    if d[n - 1] == 0:
        raise ValueError("Система не имеет однозначного решения (ноль на диагонали)")

    x[n - 1] = b[n - 1] / d[n - 1]

    # 2. Идем вверх от n-2 до 0
    for i in range(n - 2, -1, -1):
        if d[i] == 0:
            raise ValueError("Система не имеет однозначного решения (ноль на диагонали)")

        # Формула: (b_i - u_i * x_{i+1}) / d_i
        x[i] = (b[i] - u[i] * x[i + 1]) / d[i]

    return x


# --- ПРИМЕР ---
# Система:
# 2x0 + 1x1 = 5
# 3x1 + 4x2 = 18
# 5x2       = 15

diag = [2.0, 3.0, 5.0]
upper = [1.0, 4.0]
results = [5.0, 18.0, 15.0]

try:
    solution = solve_upper_bidiagonal(diag, upper, results)
    print("Решение системы:")
    for i, val in enumerate(solution):
        print(f"x{i} = {val:.2f}")
except ValueError as e:
    print(f"Ошибка: {e}")