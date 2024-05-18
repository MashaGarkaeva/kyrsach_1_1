import matplotlib.pyplot as plt
import numpy as np

file = open("C:\\Users\\мария\\PycharmProjects\\cyrsMatcad_1\\data.csv",'w')
plt.grid()
step = 2*np.pi / 99
for i in range (99):
    a = np.arange(-np.pi, np.pi, step)
    y = np.sin(a) + np.exp(a / 2)
    ser = 1 + ((3 * a) / 2) + (a ** 2 / 8) - ((7 * (a ** 3)) / 48) + (a ** 4 / 384) + ((11 * (a ** 5)) / 1280)
    + (a ** 6 / 46080) - ((127 * (a ** 7)) / 645120) + (a ** 8 / 10321920)
    result = y - ser
for val_y, val_ser, val_res in zip(y, ser, result):
    file.write(str(val_y) + '\t' + str(val_ser) + '\t' + str(val_res) + '\n')

file.close()
plt.plot( a, y, '--')
plt.plot( a, ser)
plt.plot(a, result)
plt.show()
