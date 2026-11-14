import math

def phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def cdf(z, mu=0.0, sigma=1.0):
    return phi((z - mu) / sigma)


fraction = cdf(820, 1019, 209)

print("Fraction =", fraction)