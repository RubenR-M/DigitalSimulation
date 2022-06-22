from math import e, log
from random import random
import pearson_test as pt


def poisson2numbers(lmbda, U):
    """
    > The function takes in a lambda value and a random number and returns the number of times the event
    occurs

    :param lmbda: the mean of the distribution
    :param U: a random number between 0 and 1
    :return: The number of events that occur in a given time interval.
    """

    p = e**(-lmbda)
    F = p
    i = 0

    while U > F:
        p = (lmbda*p)/(i+1)
        F += p
        i += 1

    return i


def exponential(lmbda, U):
    """
    > The function EXPONENTIAL(lmbda, U) returns a random number from the exponential distribution with
    parameter lmbda, given a random number U from the uniform distribution on (0,1)

    :param lmbda: the rate parameter of the exponential distribution
    :param U: a random number between 0 and 1
    :return: The time it takes for the next event to occur.
    """

    return -(1/lmbda)*log(U)


def binomial2numbers(n, p, U):
    """
    > The function `p2n` takes as input a probability `p`, a number of trials `n`, and a random number
    `U` and returns the number of successes `i` in `n` trials with probability of success `p`

    :param n: the number of trials
    :param p: probability of success
    :param U: a random number between 0 and 1
    :return: The number of successes in n trials.
    """

    c = p/(1-p)
    pr = (1-p)**n
    F = pr
    i = 0
    while U > F:
        pr = (c*(n-i)/(i+1))*pr
        F += pr
        i += 1

    return i


n, p = 10, .9
lmbda = 1

bins = []
pois = []
exps = []
for u in range(10):
    bin = binomial2numbers(n, p, random())
    bins.append(bin)
    poi = poisson2numbers(lmbda, random())
    pois.append(poi)
    exp = exponential(lmbda, random())
    exps.append(exp)

observedValues, expectedValues, numGroups = pt.generateObservedExpectedValues(exps, pt.EXPONENTIAL, functionParameters=[lmbda])
print(pt.pearsonTest(observedValues, expectedValues, numGroups))
