import numpy as np
def formStiffnessBernoulliBeam(GDof, numberElements, elementNodes, xx, EI, P):
    # Stiffness matrix generation for beam elements

    force = np.zeros(GDof)
    stiffness = np.zeros((GDof, GDof))
    ## print(stiffness, "\n")

    for i in range(numberElements):
        indice = elementNodes[i]
        ## print(indice)
        elementDof = np.array([2 * (indice[0]), 2 * (indice[1]) - 1, 2 * (indice[1]), 2 * (indice[1]) + 1], dtype=int)
        ## print(elementDof)
        LElem = xx[indice[1]] - xx[indice[0]]
        ##  ll = LElem
        k1 = np.array([[12, 6 * LElem, -12, 6 * LElem], [6 * LElem, 4 * LElem ** 2, -6 * LElem, 2 * LElem ** 2],
                       [-12, -6 * LElem, 12, -6 * LElem], [6 * LElem, 2 * LElem ** 2, -6 * LElem, 4 * LElem ** 2]])
        k1 = (k1 * EI) / (LElem ** 3)

        f1 = np.array([P * LElem / 2, P * LElem * LElem / 12, P * LElem / 2, -P * LElem * LElem / 12])

        k = 0
        ## print(k1, "\n")
        ## print(elementDof)
        for j in elementDof:
            force[j] = force[j] + f1[k]
            k += 1

        ##  print(force, "\n")

        k = 0
        kk = 0
        for j in elementDof:
            for jj in elementDof:
                stiffness[j, jj] = stiffness[j, jj] + k1[k, kk]
                kk += 1
            k += 1
            kk = 0

        ## print(stiffness, "\n")

    return stiffness, force

