import pandas as pd
from pandas_datareader import data
symbol = 'AMZN'
data_source='yahoo'
start_date = '2010-01-01'
end_date = '2016-01-01'

"""df = data.DataReader(symbol, data_source, start_date, end_date)

df.to_csv("amzn.csv")"""

df1 = pd.read_csv("amzn.csv")
print df1.head()

df1= df1['Close']



import matplotlib.pyplot as plt
import seaborn; seaborn.set()
df1.plot()

plt.show()



# AR example
from statsmodels.tsa.ar_model import AR
from random import random
# contrived dataset
data = [x + random() for x in range(1, 100)]
# fit model
model = AR(data)
model_fit = model.fit()
# make prediction
yhat = model_fit.predict(len(data), len(data))
print(yhat)


