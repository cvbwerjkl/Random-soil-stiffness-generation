import numpy as np
from formStiffnessBernoulliBeam import formStiffnessBernoulliBeam
from formStiffnessSpring import formStiffnessSpring
from random_gen import random_gen


def solution(Lbeam, EI, P, numberSprings, corRadius, springStiffnessMean, deviation, generations):

    tilt = np.zeros(generations)
    sAvg = np.zeros(generations)

    numberElements = numberSprings * 2  # need to be even number
    nodeCoordinates = np.linspace(0, Lbeam, num=numberElements + 1)
    L = max(nodeCoordinates)
    numberNodes = np.size(nodeCoordinates)
    xx = nodeCoordinates
    elementNodes = np.zeros((numberElements, 2), dtype=int)

    n = 0

    for i in range(numberElements):
        elementNodes[i, 0] = i
        elementNodes[i, 1] = i + 1

    #  print(elementNodes)

    GDof = 2 * numberNodes
    #  print(GDof, "\n")

    # !!!Stiffness matrix generation for beam elements
    stiffness, force = formStiffnessBernoulliBeam(GDof, numberElements, elementNodes, xx, EI, P)

    #  print(stiffness, "\n")

    corMatrix = np.zeros((numberSprings, numberSprings))

    # !!!Correlation distance matrix creation
    for i in range(numberSprings):
        for j in range(numberSprings):
            corMatrix[i, j] = -2 * abs(nodeCoordinates[1 + i * 2] - nodeCoordinates[1 + j * 2]) / corRadius

    corMatrix = np.exp(corMatrix)

    #  print(corMatrix, "\n")

    choLcorMatrix = np.linalg.cholesky(corMatrix)
    #  print(choLcorMatrix, "\n")
    kSpring = random_gen(springStiffnessMean, numberSprings, deviation, choLcorMatrix)

    #  print(kSpring, "\n")

    for i in range(generations):
        kSpring = random_gen(springStiffnessMean, numberSprings, deviation,
                             choLcorMatrix)  # generation of random stiffness for springs

        forceSpring = np.zeros(GDof + numberElements // 2)
        stiffnessSpring = np.zeros((GDof + numberSprings, GDof + numberSprings))

        # !!!Stiffness matrix generation for beam springs
        stiffnessSpring = formStiffnessSpring(GDof, kSpring, stiffnessSpring)
        #  print(stiffnessSpring, "\n")

        stiffnessSpring[:GDof, :GDof] = stiffnessSpring[:GDof, :GDof] + stiffness
        forceSpring[:GDof] = force

        # !!!Boundary conditions
        prescribedDof = np.arange(GDof, GDof + numberSprings)

        # print(stiffnessSpring, "\n")
        # print(forceSpring, "\n")

        # Solution

        U = np.delete(stiffnessSpring, prescribedDof, 0)
        U = np.delete(U, prescribedDof, 1)
        b = np.delete(forceSpring, prescribedDof, 0)

        # print(U, "\n")
        # print(b, "\n")

        displacements = np.linalg.solve(U, b)

        # !!!OUTPUT!!!

        # print(displacements[0::2], "\n")

        sAvg[n] = abs(sum(displacements[0::2]) / numberNodes)

        tilt[n] = abs((displacements[0] - displacements[-2]) / Lbeam)

        n += 1

    return sAvg, tilt
