# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---

def solve_gauss(A, b):
    """Решает СЛАУ Ax = b для квадратной матрицы A (размера n x n)"""
    n = len(A)
    # Создаем копию, чтобы не испортить исходные блоки
    mat = [row[:] + [b[i]] for i, row in enumerate(A)]

    for i in range(n):
        max_r = max(range(i, n), key=lambda r: abs(mat[r][i]))
        mat[i], mat[max_r] = mat[max_r], mat[i]
        pivot = mat[i][i]
        for j in range(i + 1, n):
            factor = mat[j][i] / pivot
            for k in range(i, n + 1):
                mat[j][k] -= factor * mat[i][k]

    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        s = sum(mat[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (mat[i][n] - s) / mat[i][i]
    return x


def mult_mat_vec(A, x):
    """Умножает квадратную матрицу на вектор"""
    n = len(x)
    return [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]


def sub_vec(a, b):
    """Вычитает вектор b из вектора a"""
    return [a[i] - b[i] for i in range(len(a))]


# --- ОСНОВНОЙ АЛГОРИТМ ---

def solve_block_bidiagonal(D, E, B):
    """
    Решает блочную нижнюю двухдиагональную СЛАУ.
    :param D: Список блоков главной диагонали (m матриц размера n x n)
    :param E: Список блоков побочной диагонали (m-1 матриц размера n x n)
    :param B: Список векторов правой части (m векторов длины n)
    :return: Список векторов решения X (m векторов длины n)
    """
    m = len(D)
    X = []

    # 1. Решаем первый блок: D_0 * X_0 = B_0
    X_0 = solve_gauss(D[0], B[0])
    X.append(X_0)

    # 2. Решаем остальные блоки по цепочке
    for i in range(1, m):
        # Вычисляем влияние предыдущего блока: E_{i-1} * X_{i-1}
        prev_effect = mult_mat_vec(E[i - 1], X[i - 1])

        # Обновляем правую часть: B_i_new = B_i - prev_effect
        rhs = sub_vec(B[i], prev_effect)

        # Решаем СЛАУ для текущего блока: D_i * X_i = rhs
        X_i = solve_gauss(D[i], rhs)
        X.append(X_i)

    return X


# --- ПРИМЕР ИСПОЛЬЗОВАНИЯ ---
# Блочный порядок m = 2, размер блоков n = 2.

# Главная диагональ: 2 блока 2x2
D_blocks = [
    [[2.0, 1.0],
     [1.0, 3.0]],  # D_0

    [[4.0, 0.0],
     [0.0, 2.0]]  # D_1
]

# Нижняя побочная диагональ: 1 блок 2x2
E_blocks = [
    [[1.0, 0.0],
     [0.0, 1.0]]  # E_0 (Единичная матрица для простоты)
]

# Векторы правой части: 2 вектора длины 2
B_vecs = [
    [5.0, 5.0],  # B_0
    [6.0, 4.0]  # B_1
]

solution = solve_block_bidiagonal(D_blocks, E_blocks, B_vecs)

print("Решение блочной системы:")
for i, x in enumerate(solution):
    print(f"X_{i} = {[round(val, 4) for val in x]}")