import numpy as np


def sumVarArray(deviation_array, springStiffnessMean_array, L_beam_array, corRadius_array):
    # summary variables array creation

    sum_var_array = np.zeros((np.size(deviation_array) * np.size(springStiffnessMean_array) * np.size(L_beam_array) * np.size(corRadius_array), 4))

    n = 0

    for i in deviation_array:
        for j in springStiffnessMean_array:
            for k in L_beam_array:
                for m in corRadius_array:
                    sum_var_array[n] = np.array([i, j, k, m])
                    n += 1

    return sum_var_array

