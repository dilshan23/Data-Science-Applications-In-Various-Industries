import numpy as np 

import matplotlib.pyplot as plt 
S0 = 100 # initial value
r = 0.05 # constant short rate
sigma = 0.25 # constant volatility
I = 10000
M = 50
T = 2.0 # in years
dt = T / M
S = np.zeros((M + 1, I))
S[0] = S0
for t in range(1, M + 1):
	S[t] = S[t - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * np.random.standard_normal(I))


plt.hist(S[-1], bins=100)
plt.xlabel('index level')
plt.ylabel('frequency')
plt.grid(True)

plt.show()



#show first 10 simulated  paths
plt.plot(S[:, :10], lw=1.5)
plt.xlabel('time')
plt.ylabel('index level')
plt.grid(True)

plt.show()