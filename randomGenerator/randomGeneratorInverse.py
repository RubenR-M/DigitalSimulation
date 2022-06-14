from math import factorial, e, log
from random import random
import numpy as np


# def poisson(lmbda, n):
#     datos = np.zeros(n)
#     datos[0] = (factorial(n) / (factorial(0) * factorial(n))) * 1 * (1-p)**(n)

#     for i in range(n-1):

#         datos[i+1] = (lmbda/(i+1)) * datos[i]

#     return datos


# def binomial(n, p):
#     """
#     It calculates the probability of each possible number of successes in a binomial distribution

#     :param n: number of trials
#     :param p: probability of success
#     :return: The probability of getting a certain number of successes in n trials.
#     """

#     datos = np.zeros(n)
#     datos[0] = (factorial(n) / (factorial(0) * factorial(n - 0))) * 1 * (1-p)**(n-0)

#     for i in range(n-1):
#         datos[i+1] = ((n-i)/(i+1)) * (p/(1-p)) * datos[i]

#     return datos


def poisson2numbers(lmbda, U):
    """
    > The function takes in a lambda value and a random number and returns the number of times the event
    occurs

    :param lmbda: the mean of the distribution
    :param U: a random number between 0 and 1
    :return: The number of events that occur in a given time interval.
    """

    # p = e**(-lambda_lb)
    # F = p
    # i = 0

    # while U < F:
    #     p = (lambda_lb*p)/(i+1)
    #     F += p
    #     i += 1

    x = -(1/lmbda)*log(U)
    return x


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


def pearson_test():
    pass


n, p = 10, .9
lmbda = 4
# Ub = binomial(n, p)
# Up = poisson(lmbda, n)
# print(Up)
# nums = []
for u in range(10):
    print(random(), " ", binomial2numbers(n, p, random()))
    print(random(), " ", poisson2numbers(0.01, random()))

# for u in Up:
#
