import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2006,1,1)
end = dt.datetime(2019,8,14)

# Get Amazon data from yahoo finance
df = web.DataReader('^NSEI','yahoo',start,end)
print(df.head())

df['Adj Close'].plot()
plt.show()