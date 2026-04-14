def gauss_jordan_solve(A, b):
    n = len(A)
    # Создаем расширенную матрицу [A | b]
    matrix = [A[i] + [b[i]] for i in range(n)]

    for i in range(n):
        # 1. Поиск главного элемента (pivoting)
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > abs(matrix[max_row][i]):
                max_row = k
        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]

        # Проверка на вырожденность
        pivot = matrix[i][i]
        if abs(pivot) < 1e-12:
            raise ValueError("Матрица вырождена или имеет бесконечно много решений")

        # 2. Делим строку на pivot, чтобы на диагонали была 1
        for j in range(i, n + 1):
            matrix[i][j] /= pivot

        # 3. Обнуляем элементы в текущем столбце для ВСЕХ строк (кроме текущей i-й)
        for k in range(n):
            if k != i:
                factor = matrix[k][i]
                for j in range(i, n + 1):
                    matrix[k][j] -= factor * matrix[i][j]

    # Результаты — это последний столбец нашей матрицы
    return [row[n] for row in matrix]

# --- ПРИМЕР ---
# Тот же пример, что и в прошлый раз:
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
    solution = gauss_jordan_solve(A_matrix, b_vector)
    print("Решение (Метод Жордана):")
    names = ['x', 'y', 'z']
    for name, val in zip(names, solution):
        print(f"{name} = {val:.4f}")
except ValueError as e:
    print(f"Ошибка: {e}")