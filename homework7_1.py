# Написать функцию, которая будет переводить градусы в радианы (без использования math.radians). Используя эту функцию,
# вывести на экран значения косинусов углов в 60, 45 и 40 градусов.
#         # returns float
#         def degrees2radians(degrees):
#         pass

import math


def degrees2radians(degrees):
    return degrees * math.pi / 180


print('Косинус угла 60 равен {0}'.format(math.cos(degrees2radians(60))))
print('Косинус угла 45 равен {0}'.format(math.cos(degrees2radians(45))))
print('Косинус угла 40 равен {0}'.format(math.cos(degrees2radians(40))))
