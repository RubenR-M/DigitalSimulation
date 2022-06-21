import numpy as np
import random as rd
from math import log, pi, cos, sin
from time import time
from scipy.stats import chisquare, chi2_contingency, norm
import matplotlib.pyplot as plt


def box_muller():

    U1 = rd.random()
    U2 = rd.random()
    R_2 = ((-2*log(U1))**.5)
    theta = 2*pi*U2

    X = R_2*cos(theta)
    Y = R_2*sin(theta)

    return X, Y


def polar():

    while True:
        U1 = rd.random()
        U2 = rd.random()
        V1 = 2*U1 - 1
        V2 = 2*U2 - 1
        S = V1**2 + V2**2
        if S <= 1:
            break
    X = ((-2*log(S)/S)**.5)*V1
    Y = ((-2*log(S)/S)**.5)*V2

    return X, Y


Xs = []
inicio = time()
for i in range(100):
    x, y = box_muller()
    Xs.append(x)
final = time()
print(final-inicio)

# plt.hist(Xs, bins=b)
# plt.show()

inicio = time()
for i in range(100):
    x, y = polar()
final = time()
print(final-inicio)