import math

def cdf(x, mu, sigma):
    z = (x - mu) / (sigma * math.sqrt(2))
    return 0.5 * (1 + math.erf(z))

mean = 1019
sigma = 209
score = 820

fraction = cdf(score, mean, sigma)

print("Probability:", fraction)
print("Percentage:", fraction * 100)