import numpy as np 


#random number between 0 and 1
print np.random.random([5])

print np.random.random([5,5])

#generate random numbers from the interval [a,b)=[5,10),

a = 5
b =10

print np.random.random([5])*(b-a)+a


# choice()  : Random sample from a given 1D array

a = [0,25,34,13]

rn4 = np.random.choice(a,100)
print rn4


###prob distributions
"""Function 	Parameters 				Description

beta 		a , b [, size ] 		Samples for beta distribution over [0, 1]
binomial 	n , p [, size ] 		Samples from a binomial distribution
chisquare 	df [, size ] 			Samples from a chi-square distribution
dirichlet 	alpha [, size ] 		Samples from the Dirichlet distribution
exponential [ scale , size ] 		Samples from the exponential distribution
f 			dfnum , dfden [, size ] Samples from an F distribution
gamma 		shape [, scale , size ] Samples from a gamma distribution
"""


sample_size = 500
rn1 = np.random.standard_normal(sample_size);print rn1
rn2 = np.random.normal(100,20,sample_size);print rn2
rn3 = np.random.chisquare(df=0.5,size = sample_size);print rn3
rn4 = np.random.poisson(lam=1.0, size=sample_size);print rn4  #posiison  :simulatre arrival ofrare events like a jump in the price of external events

#plot

import matplotlib.pyplot as plt 

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2,
figsize=(7, 7))
ax1.hist(rn1, bins=25)
ax1.set_title('standard normal')
ax1.set_ylabel('frequency')
ax1.grid(True)

ax2.hist(rn2, bins=25)
ax2.set_title('normal(100, 20)')
ax2.grid(True)

ax3.hist(rn3, bins=25)
ax3.set_title('chi square')
ax3.set_ylabel('frequency')
ax3.grid(True)

ax4.hist(rn4, bins=25)
ax4.set_title('Poisson')
ax4.grid(True)


plt.show()
