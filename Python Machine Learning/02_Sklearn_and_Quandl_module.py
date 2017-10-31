# sklearn is a Python module integrating classical machine
# learning algorithms in the tightly-knit world of scientific Python
# packages (numpy, scipy, matplotlib).
# It aims to provide simple and efficient solutions to learning problems
# that are accessible to everybody and reusable in various contexts:
# machine-learning as a versatile tool for science and engineering.
# python.exe -m pip install sklearn

# Get millions of financial and economic datasets from hundreds of publishers directly into Python.
# python.exe -m pip install quandl

import pandas as pd
import quandl
import math

df = quandl.get('WIKI/GOOGL')

# to get ytpes of values each dataframe colum holds
# print(df.dtypes)

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HighLow Percent'] = (df['Adj. High'] - df['Adj. Close'])/ df['Adj. Close'] * 100.0
df['Percent Change'] = (df['Adj. Close'] - df['Adj. Open'])/ df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HighLow Percent', 'Percent Change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))

df['Forecast'] = df[forecast_col].shift(-forecast_out)
print(df.head(5))
