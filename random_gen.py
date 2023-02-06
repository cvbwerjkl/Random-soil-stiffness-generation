# generate a series of txt files with random numbers according to a specify probability properties

#  import random
import numpy as np


def random_gen(stiffnessMean, numberSprings, deviation, choLcorMatrix):
    a_b = stiffnessMean  # basic normal distribution parameter mean
    b_b = a_b * deviation  # basic normal distribution parameter standard deviation
    n = numberSprings  # number ov elements

    # kSpring = np.empty([n])

    a = a_b / n  # normal distribution parameter mean with elements number correlation
    b = b_b / n  # normal distribution parameter standard deviation with elements number correlation

    kSpring = np.random.normal(0, 1, n)

    kSpring = np.matmul(choLcorMatrix, np.transpose(kSpring))

    kSpring = kSpring * b + a

    #  for ii in range(n):
    #    kSpring[ii] = abs(random.gauss(a, b))

    return kSpring
