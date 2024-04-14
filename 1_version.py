import math
from array import array
import matplotlib.pyplot as plt
import numpy as np


file = open("C:\\Users\\мария\\PycharmProjects\\cyrsMatcad_1\\data_csv.csv",'w')
plt.grid()
for i in range (99):
    x = np.linspace(-3.14, 3.14)
    y = np.sin(x) + np.exp(x/2)
file.writelines(str(y))

file.close()
plt.plot( x, y, '--')


plt.show()
'''
x = []
y = []
up = []
low = []
start = -3.14
end = 3.14
step = (3.14 + 3.14) / 99

current = start
while current <= end:
    x.append(current)

    sin_x = math.sin(current * 12) * 5

    sin_ul = math.sin(current) + 2
    up.append(sin_ul)

    sin_ll = -sin_ul - 2
    low.append(sin_ll)

    # Повторение изгибов up и low
    if sin_ll <= sin_x <= sin_ul:
        y.append(sin_x)
    elif sin_x < sin_ll:
        y.append(sin_ll)
    else:
        y.append(sin_ul)

    current += step

plt.plot(x, y, '--')
plt.plot(x, up)
plt.plot(x, low)
plt.show()'''