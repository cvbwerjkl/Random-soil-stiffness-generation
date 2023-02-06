import numpy as np


def formStiffnessSpring(GDof, kSpring, stiffnessSpring):
    # Stiffness matrix generation for beam springs

    n = GDof
    nn = 2
    p = 0
    for s in range(2, GDof - 2, 4):
        kkSpring = kSpring[p]
        spring = np.array([[kkSpring, - kkSpring], [-kkSpring, kkSpring]])
        p += 1
        k = 0
        kk = 0
        for j in (nn, n):
            for jj in (nn, n):
                stiffnessSpring[j, jj] = stiffnessSpring[j, jj] + spring[k, kk]
                kk += 1
            k += 1
            kk = 0
        n += 1
        nn += 4

    return stiffnessSpring

