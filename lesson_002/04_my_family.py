#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Complete!

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['mother','father','sister','grandmother1','grandmother2','grandfather','dog','cat']


# список списков приблизителного роста членов вашей семьи
my_f_h = [
    # ['имя', рост],
    ['Александр', 184],['Артем',178],['Макс',175],['Оля',168],['Саша',170]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print('Рост отца -',my_f_h[0][1],'cм')
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
all_h = (my_f_h[0][1] + my_f_h[1][1] + my_f_h[2][1] + my_f_h[3][1] + my_f_h[4][1])
all_h2 = (my_f_h[0][1] + my_f_h[1][1] + my_f_h[2][1] + my_f_h[3][1] + my_f_h[4][1])/5
print(all_h)
print(all_h2)