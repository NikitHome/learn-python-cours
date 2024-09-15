# Числа очень часто применяются в программировании для ведения счета в играх, 
# предоставления данных в визуализациях, хранения информации в веб-приложениях и 
# т.д. В Python числовые данные делятся на несколько категорий в соответствии со 
# способом их использования. 

number_0 = 555
print(number_0)

# В записи целых чисел можно группировать цифры при помощи символов 
# подчеркивания, чтобы числа лучше читались.
number_00 = 100_000_000_000 # нижнее подчеркивание испаользуется для 
                                   # визуального разделения на разряды
# При выводи числа, определяемого с символами подчеркивания. Python выводит 
# только цифры.
print(number_00)

# В Python с целыми числами можно выполнять операции сложения (+), вычитания 
# (-), умножения (*) и деления (/).

number_1 = 5 + 8 # сложение
print(number_1)

number_2 = 8 - 3 # вычитание
print(number_2)

number_3 = 8 * 6 # умножение
print(number_3)

number_4 = 8 / 2 # деление
print(number_4)

number_5 = 8 % 3 # остаток от деления
print(number_5)

number_6 = 8 // 3 # целая часть от деления
print(number_6)

number_7 = 8 ** 3 # возведение в степень
print(number_7)

# В Python также существует определенный порядок операций, что позволяет 
# использовать несколько операций в одном выражении. Круглые скобки 
# используются для изменения следования операций, чтобы выражение могло 
# вычислятся в нужном порядке.

number_8 = 2 + 3 * 4
print(number_8)

number_9 = (2 + 3) * 4
print(number_9)

# В Python числа имеющие дробную часть, называются вещественными (или "числа с 
# плавающей точкой"). Обычно разработчик может просто воспользоватся дробными 
# значениями, не особо задумываясь об их поведении. Просто введите нужные числа, 
# а Python, скорее всего, сделает именно то, что вы от него хотите.

number_10 = 0.1 + 0.1
print(number_10)

number_11 = 2 * 0.4
print(number_11)

# При делении двух любых чисел - даже если это целые числа, частным от деления 
# которых является целое число, - вы всегда получаете вещественное число.

# При смешении целого и вещественного числа в любой другой операции вы также 
# получаете вещественное число.

number_12 = 4 / 2
print(number_12)

# Python по умолчанию использует вещественный тип для результата любой операции, 
# в которой задействовано вещественное число, даже если результат является 
# целым числом.