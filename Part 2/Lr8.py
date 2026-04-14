def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def subtract(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def strassen(A, B):
    n = len(A)

    # Базовый случай: если матрица 1x1
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # 1. Разделение матриц на четверти
    mid = n // 2
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]

    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]

    # 2. Вычисление 7 произведений Штрассена (P1 - P7)
    p1 = strassen(add(A11, A22), add(B11, B22))
    p2 = strassen(add(A21, A22), B11)
    p3 = strassen(A11, subtract(B12, B22))
    p4 = strassen(A22, subtract(B21, B11))
    p5 = strassen(add(A11, A12), B22)
    p6 = strassen(subtract(A21, A11), add(B11, B12))
    p7 = strassen(subtract(A12, A22), add(B21, B22))

    # 3. Сборка результирующей матрицы из P
    # C11 = P1 + P4 - P5 + P7
    c11 = add(subtract(add(p1, p4), p5), p7)
    # C12 = P3 + P5
    c12 = add(p3, p5)
    # C21 = P2 + P4
    c21 = add(p2, p4)
    # C22 = P1 - P2 + P3 + P6
    c22 = add(subtract(add(p1, p3), p2), p6)

    # Объединяем четверти в одну матрицу
    result = []
    for i in range(mid):
        result.append(c11[i] + c12[i])
    for i in range(mid):
        result.append(c21[i] + c22[i])

    return result


# --- ПРИМЕР ---
# Матрицы должны быть n x n, где n - степень двойки
mat_A = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 1, 2, 3],
    [4, 5, 6, 7]
]

mat_B = [
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 0, 1, 1]
]

res = strassen(mat_A, mat_B)

print("Результат умножения Штрассена:")
for row in res:
    print(row)