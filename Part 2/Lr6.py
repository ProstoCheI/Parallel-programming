def gauss_solve(A, b):
    n = len(A)
    # Формируем расширенную матрицу [A | b]
    matrix = [A[i] + [b[i]] for i in range(n)]

    # --- ПРЯМОЙ ХОД ---
    for i in range(n):
        # 1. Поиск главного элемента в i-м столбце (для стабильности)
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k

        # Меняем строки местами
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Проверка на вырожденность
        if abs(matrix[i][i]) < 1e-12:
            raise ValueError("Система не имеет однозначного решения (матрица вырождена)")

        # 2. Обнуление элементов под текущим диагональным элементом
        for k in range(i + 1, n):
            factor = matrix[k][i] / matrix[i][i]
            for j in range(i, n + 1):
                matrix[k][j] -= factor * matrix[i][j]

    # --- ОБРАТНЫЙ ХОД ---
    x = [0] * n
    for i in range(n - 1, -1, -1):
        # Сумма произведений уже найденных x на коэффициенты
        sum_ax = sum(matrix[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (matrix[i][n] - sum_ax) / matrix[i][i]

    return x


# --- ПРИМЕР ---
# 3x + 2y - z  = 1
# 2x - 2y + 4z = -2
# -x + 0.5y - z = 0

A_matrix = [
    [3.0, 2.0, -1.0],
    [2.0, -2.0, 4.0],
    [-1.0, 0.5, -1.0]
]
b_vector = [1.0, -2.0, 0.0]

try:
    solution = gauss_solve(A_matrix, b_vector)
    print("Решение системы:")
    names = ['x', 'y', 'z']
    for name, val in zip(names, solution):
        print(f"{name} = {round(val, 4)}")
except ValueError as e:
    print(f"Ошибка: {e}")