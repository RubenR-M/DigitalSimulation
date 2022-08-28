import math
import numpy as np
from random import random


def logisticPDF(parameters, bins):
    """
    It takes in two parameters, the first of which is the location of the peak of the logistic function,
    and the second of which is the width of the logistic function. It then returns the logistic function
    evaluated at the bins

    :param parameters: [mu, sigma]
    :param bins: the x-axis of the histogram
    :return: The logistic function.
    """

    num = np.exp(-(bins-parameters[0])/parameters[1])
    den = parameters[1]*(1 + num)**2

    return num/den


def logisticCDF(parameters, bins):
    """
    The logistic CDF is the cumulative distribution function of the logistic distribution

    :param parameters: [mu, sigma]
    :param bins: the x-axis of the histogram
    :return: The logistic CDF is being returned.
    """

    num = np.exp(-(bins-parameters[0])/parameters[1])
    cdf = 1/(1 + num)

    return cdf


def inverseLogistic(mu, s):
    """
    It generates a random number from a logistic distribution.

    :param mu: the mean of the distribution
    :param s: the standard deviation of the distribution
    """

    x = 2*s*np.arctanh(2*random() - 1) + mu
    return x


def logisticInverse(mu, sigma, p):
    """
    > The logistic inverse function takes a mean, a standard deviation, and a probability, and returns
    the value of the random variable that corresponds to that probability

    :param mu: the mean of the logistic distribution
    :param sigma: the standard deviation of the logistic distribution
    :param p: the probability of success
    :return: The logistic inverse function is being returned.
    """

    Q = mu + sigma*math.log(p/(1-p))
    return Q
