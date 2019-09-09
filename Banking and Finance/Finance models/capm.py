"""capital asset pricing model
CAPM, the relationship between risk and rates of returns in a security """


""" Linear regression with SciPy """
from scipy import stats

stock_returns = [0.065, 0.0265, -0.0593, -0.001, 0.0346]

mkt_returns = [0.055, -0.09, -0.041, 0.045, 0.022]

beta, alpha, r_value, p_value, std_err = stats.linregress(stock_returns, mkt_returns)

print beta
