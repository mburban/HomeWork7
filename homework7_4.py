# Написать функцию, которая вычислит площадь основания и объем конуса по его радиусу и высоте. Функция должна вернуть
# два значения
#         # returns 2 floats
#         def cone_square_and_volume(radius, height):
#         pass


def cone_square_and_volume(radius, height):
    import math
    cone_square = math.pi * (radius**2)
    cone_volume = cone_square * height / 3
    return cone_square, cone_volume


cone_height = int(input('Введите высоту конуса: '))
cone_radius = int(input('Введите радиус конуса: '))
cone_square, cone_volume = cone_square_and_volume(cone_radius, cone_height)
print('Площадь основания конуса равна {0}, а его объем равен {1}.'.format(cone_square, cone_volume))
