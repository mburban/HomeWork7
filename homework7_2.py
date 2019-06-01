# Написать функцию, которая рассчитывает сумму всех цифр некоторого трехзначного числа, введенного пользователем в
# консоли, без использования операторов цикла. a) cо строками, б) без использования строк.
#         # returns int
#         def sum_of_digits(number):
#         pass


def sum_of_digits_by_string(number):
    digit_a = str(number[0])
    digit_b = str(number[1])
    digit_c = str(number[2])
    sum_digits = int(digit_a) + int(digit_b) + int(digit_c)
    return sum_digits


def sum_of_digits_by_math(number):
    digit_a = int(number) // 100
    digit_b = int(number) // 10 % 10
    digit_c = int(number) % 10
    sum_digits = digit_a + digit_b + digit_c
    return sum_digits


user_number = input('Введите трехзначное число: ')
if int(user_number) < 100 or int(user_number) > 999:
    print('Вы ввели некорректное числою')
else:
    print('Расчет суммы всех цифр используя строки: {0}'.format(sum_of_digits_by_string(user_number)))
    print('Расчет суммы всех цифр без использования строк: {0}'.format(sum_of_digits_by_math(user_number)))
