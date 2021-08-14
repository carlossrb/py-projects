import numpy as np
import time as time
import matplotlib.pyplot as plt
from gaussJordan import GaussJordan as gj

initial = 2
final = 100
times_gauss = []
times_numpy = []
for i in range(initial, final):
    A = np.random.randint(-5, 5, size=(i, i))
    b = np.random.randint(-5, 5, size=(i))
    if np.linalg.det(A) != 0:
        inicio = time.time()
        xgauss = gj(A, b)
        fim = time.time()
        times_gauss.append((fim-inicio)*1000)  # tempo em s
        inicio = time.time()
        xnump = np.linalg.solve(A, b)
        fim = time.time()
        times_numpy.append((fim-inicio)*1000)  # tempo em s
print('ACABOU')
plt.title("Tempo de execução")
plt.xlabel("Passo")
plt.ylabel("Tempo (s)")

df = {'x_values': np.arange(initial, final),
      'y1_values': times_gauss, 'y2_values': times_numpy}

plt.plot('x_values', 'y1_values', data=df, marker='',
         color='olive', linewidth=2, label="gauss")
plt.plot('x_values', 'y2_values', data=df, marker='', color='blue',
         linewidth=2, linestyle='dashed', label="numpy")
# show legend
plt.legend()

plt.show()
