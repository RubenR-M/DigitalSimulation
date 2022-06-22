"""
Runs Test implementation
"""

from math import erfc
import numpy as np


def lfsrF(end):
    start_state = 1 << 15 | 1
    lfsr = start_state
    period = 0

    datos = []

    while period < end:
        # taps: 16 15 13 4; feedback polynomial: x^16 + x^15 + x^13 + x^4 + 1
        bit = (lfsr ^ (lfsr >> 1) ^ (lfsr >> 3) ^ (lfsr >> 12)) & 1
        lfsr = (lfsr >> 1) | (bit << 15)
        datos.append(lfsr)
        period += 1
        if (lfsr == start_state):
            print(period)
            break

    return datos


def runsTest(epsilon):

    n_ones = epsilon.count("1")
    lenEpsilon = len(epsilon)
    proportion = n_ones/lenEpsilon
    tau = 2/(lenEpsilon)**0.5

    if abs(proportion - 1/2) >= tau:
        return False

    stat_test = n_ones + 1

    numerator = abs(stat_test - 2*lenEpsilon*proportion*(1 - proportion))
    denominator = 2*((2*lenEpsilon)**0.5)*proportion*(1 - proportion)

    pValue = erfc(numerator/(denominator + 2**-52))

    print(f"""
        n:{lenEpsilon}
        proportion:{proportion}
        #1:{n_ones}
        tau:{tau}
        V:{stat_test} 
        pValue:{pValue}
    """)

    if pValue >= 0.01:
        return True
    else:
        return False


def main():
    test = "1100100100001111110110101010001000100001011010001100001000110100110001001100011001100010100010111000"

    datos = np.array(lfsrF(5))

    print(datos)
    epsilon = ""
    for num in datos:
        epsilon += format(num, "b")

    print("\t\nEpsilon: " + epsilon)
    result = runsTest(epsilon)
    print(f"\tThe sequence is random?\n\tRTA:{result}\n")


if __name__ == "__main__":
    main()
