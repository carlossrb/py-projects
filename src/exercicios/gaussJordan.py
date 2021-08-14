import numpy as np


def GaussJordan(A, b):
    b = np.array(b, dtype=float)
    A = np.array(A, dtype=float)
    Ab = np.column_stack((A, b))
    n = np.shape(Ab)[0]
    m = np.shape(Ab)[1]
    for i in range(0, n - 1, 1):
        if Ab[i, i] == 0:
            print("Divisao por zero")
            break
        for k in range(i + 1, n, 1):
            fator = Ab[k, i] / Ab[i, i]
            Ab[k, :] = Ab[k, :] - Ab[i, :] * fator
    for i in range(n - 1, -1, -1):
        for k in range(i - 1, -1, -1):
            fator = Ab[k, i] / Ab[i, i]
            Ab[k, :] = Ab[k, :] - Ab[i, :] * fator
        Ab[i, :] = Ab[i, :] / Ab[i, i]
    x = np.copy(Ab[:, m - 1])
    return x
