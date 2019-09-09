"""Pricing European options
Consider a two-step binomial tree. A non-dividend paying stock price starts at $50,
and in each of the two time steps, the stock may go up by 20 percent or go down by
20 percent. We suppose that the risk-free rate is 5 percent per annum and the time to
maturity T is 0.5 years. 

We would like to find the value of an European put option
with a strike price K of $52.

The following figure shows the pricing of the stock using a binomial tree:
"""


#stockOption class to store and calculate the common
#attributes of the stock option
import math
class StockOption:

	def __init__(self,S0,K,r,T,N,params):

		self.S0 = S0 #spot price
		self.K = K#strike price
		self.r = r#risk-free rate
		self.T = T#time to maturity
		self.N = max(1,N)   #ensure N have at least 1 time step
		self.STs = None # Declare the stock prices tree

		""" Optional parameters used by derived classes """

		self.pu = params.get("pu",0)  # probability of up state  ...... dictionary method:get()  if no vslue is reutrned ite 0
		self.pd = params.get("pd",0)   # probability of down state

		self.div = params.get("div", 0) # Dividend yield
		self.sigma = params.get("sigma", 0) # Volatility
		self.is_call = params.get("is_call", True) # Call or put
		self.is_european = params.get("is_eu", True) # Eu or Am

		""" Computed values """
		self.dt = T/float(N) # Single time step, in years
		self.df = math.exp(
		-(r-self.div) * self.dt) # Discount factor





		
