import math
import numpy as np 
from time import time

np.random.seed(20000)
t0 = time()

#parameters

S0 = 100.; K = 105.; T = 1.0; r = 0.05; sigma = 0.2
M = 50; dt = T / M; I = 250000

# Simulating I paths with M time steps

S = np.zeros((M+1,I))

S[0] = S0

print S

for t in range(1,M+1):

	z = np.random.standard_normal(I)

	print z

	S[t] = S[t-1] * np.exp((r-0.5*sigma**2)*dt + sigma*math.sqrt(dt)*z)  #Euler discretization of SDE

	print S[t]

print S[-1]
print np.maximum(S[-1] - K, 0)

print np.sum(np.maximum(S[-1] - K, 0)) / I
# Calculating the Monte Carlo estimator
C0 = math.exp(-r * T) * np.sum(np.maximum(S[-1] - K, 0)) / I
# Results output
tnp1 = time() - t0

print "European Option Value %7.3f" % C0
print "Duration in Seconds %7.3f" % tnp1

