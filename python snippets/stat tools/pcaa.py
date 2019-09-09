import numpy as np
import pandas as pd
from pandas_datareader import data 
from sklearn.decomposition import KernelPCA

symbols = ['ADS.DE',
'BMW.DE',
'DBK.DE',
'FRE.DE',
'LIN.DE',
'SAP.DE',
'^GDAXI',
'ALV.DE',
'CBK.DE',
'DPW.DE',
'HEI.DE',
'LXS.DE',
'SDF.DE',
'BAS.DE', 'BAYN.DE', 'BEI.DE',
'CON.DE', 'DAI.DE', 'DB1.DE',
'DTE.DE', 'EOAN.DE', 'FME.DE',
'HEN3.DE', 'IFX.DE', 'LHA.DE',
'MRK.DE', 'MUV2.DE', 'RWE.DE',
'SIE.DE', 'TKA.DE', 'VOW3.DE',]
"""
df = pd.DataFrame()
for sym in symbols:
	df[sym] = data.DataReader(sym, data_source='yahoo')['Close']
df = df.dropna()

df.to_csv("germanindex.csv")"""


df = pd.read_csv("germanindex.csv")

print df.head()


dax = pd.DataFrame(df.pop('^GDAXI'))

"""Applying PCA
Usually, PCA works with normalized data sets. Therefore, the following convenience
function proves helpful:"""



scale_function = lambda x:(x - x.mean()) /x.std()

pca = KernelPCA().fit(df.apply(scale_function))

print len(pca.lambdas_)