
# Вычислить число c заданной точностью d

# Пример:

# - при d = 0.001, π = 3.141   
# Ввод: 0.01
#     Вывод: 3.14

#     Ввод: 0.001
#     Вывод: 3.141



import math
pi = math.pi
d = float(input('как округляем?(вид 0.0..01) '))

c = 0
while d < 1:
    c += 1
    d = d*10
print(round(pi, c))