import numpy as np
import random as rd
from math import e, pi, log


def reject(c, f, g) -> float:
    """
    > The function `reject` takes in three functions `c`, `f`, and `g` and returns a random number `x`
    and a list of random numbers `Y` that were generated in the process of generating `x`

    :param c: constant
    :param f: the function we want to sample from
    :param g: the pdf of the random variable we want to sample from
    :return: the value of x and the list of Y values.
    """

    Y = []
    x = 0
    while True:
        y = -1*log(rd.random())
        Y.append(y)
        U = rd.random()
        condition = eval(f) / c*eval(g)
        if U <= condition:
            x = y
            break
    return x, Y


c = (2*e/pi)**.5
f = "(2/(2*pi)**.5)*e**(-(y**2)/2)"
g = "e**(-x)"

Ys = []
Xs = []
for i in range(100):
    x, y = reject(c, f, g)
    Ys = np.concatenate([Ys, y])
    Xs.append(x)
