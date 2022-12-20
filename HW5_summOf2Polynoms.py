# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными.
# Степени многочленов могут отличаться.

import re

with open("polynom_5hw_file1.txt", "r") as file1:
    polynom1 = file1.read()

with open("polynom_5hw_file2.txt", "r") as file2:
    polynom2 = file2.read()

print(f"формула № 1 = {polynom1}")
print(f"формула № 2 = {polynom2}")

polynom_sum = polynom2.replace("= 0", "") + polynom1.replace(" = 0", "")

polynom_sum = re.split(r'[\s]', polynom_sum)

temp_lst = []
for i in range(len(polynom_sum)):
    temp_lst.append(polynom_sum[i].split("*x"))

dkt_temp = {}
for i, item in enumerate(temp_lst):
    if len(item) == 2:
        if item[1] in dkt_temp and temp_lst[i-1] == list(['+']):
            dkt_temp[item[1]] += int(item[0])
        elif item[1] in dkt_temp and temp_lst[i-1] == list(['-']):
            dkt_temp[item[1]] -= int(item[0])
        else:
            dkt_temp[item[1]] = int(item[0])

new_poly = []
for i, (k, w) in enumerate(dkt_temp.items()):
    if w > 0 and i != 0:
        new_poly.append(f"+ {w}*x{k}")
    elif w > 0 and i == 0:
        new_poly.append(f"{w}*x{k}")
    elif w < 0:
        new_poly.append(f"- {abs(w)}*x{k}")
    else:
        continue

formula = ' '.join(new_poly) + ' = 0'

with open("5hw_sum_of_polynoms.txt", "w", encoding='UTF-8') as file:
    file.write(f"Сумма формул => {formula}")