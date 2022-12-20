# Вычислить число π c заданной точностью d
# *Пример:*
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


def truncate(f, n):
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

def check_d(d):
    degree_d = 0
    while d != 1:
        d = d * 10
        degree_d += 1
    return degree_d


d = float(str(input("Введи точность Пи, глубину цифр после точки (0.01) = ")).replace(",", "."))
d = check_d(d)
pi = 2 * (3 ** 0.5)
k = 1
for i in range(1, d+1):
    k += (1 / (((2 * i + 1)) * ((-3) ** i)))
pi = pi * k

print(truncate(pi, d))




