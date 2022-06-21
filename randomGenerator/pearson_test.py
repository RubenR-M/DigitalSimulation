import numpy as np
from math import log
import scipy.stats as stat2


def EXPONENTIAL(lmbda, bins):
    return 1 - np.exp(-lmbda[0]*bins)


def generateObservedExpectedValues(generatedValues, functionName, functionParameters=[]):

    numGroups = round(1 + log(len(generatedValues))/log(2))
    maxValue = max(generatedValues)

    observedValues, bins = np.histogram(generatedValues, bins=numGroups)
    # print(numGroups, observedValues, bins)

    probs = functionName(functionParameters, bins)
    probsExp = []

    for i in range(1, numGroups+1):
        probsExp.append(probs[i] - probs[i-1])
    # print(probsExp)
    expectedValues = np.array(probsExp)*len(generatedValues)

    return observedValues, expectedValues, numGroups


def pearsonTest(observedValues, expectedValues, numGroups):
    est_chi = 0

    for k in range(numGroups):
        est_chi = est_chi + ((observedValues[k] - expectedValues[k])**2)/expectedValues[k]

    result = stat2.chisquare(observedValues, expectedValues, numGroups - 1, axis=None)
    print(result.statistic)
    print(est_chi)
    print(stat2.chi2.cdf(est_chi, numGroups - 1))
    print(stat2.chi2.cdf(result.statistic, numGroups - 1))
