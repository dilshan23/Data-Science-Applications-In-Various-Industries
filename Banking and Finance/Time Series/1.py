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


