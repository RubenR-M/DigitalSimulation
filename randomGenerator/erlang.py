from math import e, log, factorial
from random import random
import pearson_test as pt


def earlangCDF(parameters: list, bins: list) -> float:
    """
    The function takes in a list of parameters and a list of bins, and returns the CDF of the Erlang
    distribution.

    :param parameters: list
    :type parameters: list
    :param bins: the x-axis values
    :type bins: list
    :return: The CDF of the Erlang distribution.
    """

    cdf = 0
    for i in range((parameters[1] - 1)):
        cdf += (1/factorial(i))*(e**(-parameters[0]*bins))*((parameters[0]*bins)**i)

    cdf = 1 - cdf
    return cdf


def earlangGenerator(lmbda: float, iterations: int) -> float:
    """
    It generates a random number from an exponential distribution with a given lambda

    :param lmbda: the rate of the exponential distribution
    :type lmbda: float
    :param iterations: number of iterations to run the simulation
    :type iterations: int
    :return: The sum of the random variables.
    """

    earlang = 0
    for i in range(iterations):
        U = random()
        earlang += (-1/lmbda)*log(U)

    return earlang


lmbda = 0.5
iterations = 10

earlangs = []

for u in range(10):
    earlang = earlangGenerator(lmbda, iterations)
    earlangs.append(earlang)

# print(earlangs)

observedValues, expectedValues, numGroups = pt.generateObservedExpectedValues(earlangs, earlangCDF, functionParameters=[lmbda, iterations])
# print(observedValues, expectedValues, numGroups)
print(pt.pearsonTest(observedValues, expectedValues, numGroups, 2))
