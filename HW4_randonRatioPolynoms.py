# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
#  и записать в файл многочлен степени k.
#
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

k = int(input("Введи максимальную натуральную степень k = "))

polynom_list = []
for i in range(k, 0, -1):
    temp_lst = []
    num = randint(0, 100)
    if num < 0 and i != 1:
        polynom_list.append("-")
        num = abs(num)
        temp_lst.append(str(num))
        temp_lst.append("*x**")
        temp_lst.append(str(i))
    elif num > 0 and i != 1:
        polynom_list.append("+")
        temp_lst.append(str(num))
        temp_lst.append("*x**")
        temp_lst.append(str(i))
    elif num < 0 and i == 1:
        polynom_list.append("-")
        num = abs(num)
        temp_lst.append(str(num))
        temp_lst.append("*x")
    elif num > 0 and i == 1:
        polynom_list.append("+")
        temp_lst.append(str(num))
        temp_lst.append("*x")
    elif num == 0:
        continue
    polynom_list.append("".join(temp_lst))

print(polynom_list)

if polynom_list[0] != "-":
    polynom_list.pop(0)
formula = ' '.join(polynom_list) + ' = 0'

print(formula)


with open("polynom_4hw.txt", "w") as file:
    file.write(f"k={k} => {formula}")