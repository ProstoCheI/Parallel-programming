def horner_method(coefficients, x):
    """
    Вычисляет значение многочлена по схеме Горнера.

    :param coefficients: Список коэффициентов [a_n, a_{n-1}, ..., a_0]
    :param x: Точка, в которой вычисляем значение
    :return: Результат вычисления
    """
    # Инициализируем результат первым коэффициентом
    result = coefficients[0]

    # Проходим по остальным коэффициентам
    # Начинаем со второго элемента (индекс 1)
    for i in range(1, len(coefficients)):
        result = result * x + coefficients[i]

    return result


# Пример использования:
# Многочлен: 2x^3 - 6x^2 + 2x - 1
# Коэффициенты: [2, -6, 2, -1]
# Точка x = 3
poly_coeffs = [2, -6, 2, -1]
target_x = 3

final_value = horner_method(poly_coeffs, target_x)

print(f"Значение многочлена в точке x = {target_x} равно: {final_value}")