# Пользователь вводит длины катетов прямоугольного треугольника. Написать функцию, которая вычислит площадь треугольника
# и его периметр. Функция должна вернуть два значения.
#         # returns 2 values
#         def triangle_square_and_perimeter(a, b):
#         pass


def triangle_square_and_perimeter(a, b):
    import math
    triangle_hypotenuse = math.sqrt((a**2) + (b**2))
    triangle_square = a * b / 2
    triangle_perimeter = a + b + triangle_hypotenuse
    return triangle_square, triangle_perimeter


cathetus1 = int(input('Введите первый катет: '))
cathetus2 = int(input('Введите второй катет: '))
triangle_square, triangle_perimeter = triangle_square_and_perimeter(cathetus1, cathetus2)
print('Площадь прямоугольного треугольника равна {0}, а его периметр равен {1}.'.format(triangle_square,
                                                                                        triangle_perimeter))
