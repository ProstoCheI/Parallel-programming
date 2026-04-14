def transpose(matrix):
    """Транспонирует матрицу (строки становятся столбцами)."""
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]


def add_matrices(A, B):
    """Складывает две матрицы одинакового размера."""
    rows = len(A)
    cols = len(A[0])
    return [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]


def multiply_matrices(A, B):
    """Умножает две матрицы A (m x n) и B (n x p)."""
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    # Создаем пустую матрицу нужного размера
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result


def solve_expression(A, B):
    """Вычисляет A.T * (B + B.T) * A"""
    # 1. Находим B^T
    BT = transpose(B)

    # 2. Находим S = B + B^T
    S = add_matrices(B, BT)

    # 3. Находим M = S * A
    M = multiply_matrices(S, A)

    # 4. Находим AT = A^T
    AT = transpose(A)

    # 5. Финальный результат: AT * M
    result = multiply_matrices(AT, M)
    return result


# --- ПРИМЕР ---
matrix_A = [
    [1, 2],
    [3, 4]
]

matrix_B = [
    [0, 1],
    [2, 3]
]

res = solve_expression(matrix_A, matrix_B)

print("Результат A^T(B + B^T)A:")
for row in res:
    print(row)