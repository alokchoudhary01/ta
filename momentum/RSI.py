######################################################
# Stock Technical Analysis with Python               #
# Simple Moving Average SMA(5)                       #
# (c) Diego Fernandez Garcia 2015-2017               #
# www.exfinsis.com                                   #
######################################################

# 1. Packages and Data

# Packages Importing
import numpy as np
import pandas as pd
# import pandas_datareader.data as web
import matplotlib.pyplot as plt
import ta as ta

# Data Downloading or Reading

# Google Finance
# No Adjusted Close Prices
# spy = web.DataReader('SPY', 'google', '2016-01-01', '2017-01-01')
# spy['Adj Close'] = spy['Close']

# Yahoo Finance
# spy = web.DataReader('SPY', 'yahoo', '2016-01-01', '2017-01-01')

# Data Reading
spy = pd.read_csv("StockTechnicalData.txt", index_col='Date', parse_dates=True)

##########

# 2. Simple Moving Average SMA(5) Calculation and Chart
# Technical Indicator Calculation
spy['sma5'] = ta.SMA(np.asarray(spy['Close']), 5)
# Technical Indicator Chart
spy.plot(y=['Close', 'sma5'])
plt.title('SPY Close Prices & Simple Moving Average SMA(5)')
plt.legend(loc='upper left')
plt.show()

##########

# 3. Price Crossover Trading Signals
# Previous Periods Data (avoid backtesting bias)
spy['Close(-1)'] = spy['Close'].shift(1)
spy['sma5(-1)'] = spy['sma5'].shift(1)
spy['Close(-2)'] = spy['Close'].shift(2)
spy['sma5(-2)'] = spy['sma5'].shift(2)
# Generate Trading Signals (buy=1 , sell=-1, do nothing=0)
spy['sma5sig'] = 0
sma5sig = 0
for i, r in enumerate(spy.iterrows()):
    if r[1]['Close(-2)'] < r[1]['sma5(-2)'] and r[1]['Close(-1)'] > r[1]['sma5(-1)']:
        sma5sig = 1
    elif r[1]['Close(-2)'] > r[1]['sma5(-2)'] and r[1]['Close(-1)'] < r[1]['sma5(-1)']:
        sma5sig = -1
    else:
        sma5sig = 0
    spy.iloc[i, 11] = sma5sig
# Trading Signals Chart
fig1, ax = plt.subplots(2, sharex=True)
ax[0].plot(spy['Close'])
ax[0].plot(spy['sma5'])
ax[0].legend(loc='upper left')
ax[1].plot(spy['sma5sig'], marker='o', linestyle='')
ax[1].legend(loc='upper left')
plt.suptitle('SPY Close Prices & Simple Moving Averages SMA(5 & 21)')
plt.show()

##########

# 4. Price Crossover Trading Strategy
# Generate Trading Strategy (own stock=1 , not own stock=0, short-selling not available)
spy['sma5str'] = 1
sma5str = 0
for i, r in enumerate(spy.iterrows()):
    if r[1]['sma5sig'] == 1:
        sma5str = 1
    elif r[1]['sma5sig'] == -1:
        sma5str = 0
    else:
        sma5str = spy['sma5str'][i-1]
    spy.iloc[i, 12] = sma5str
# Trading Strategy Chart
fig2, ax = plt.subplots(2, sharex=True)
ax[0].plot(spy['Close'])
ax[0].plot(spy['sma5'])
ax[0].legend(loc='upper left')
ax[1].plot(spy['sma5str'], marker='o', linestyle='')
ax[1].legend(loc='upper left')
plt.suptitle('SPY Close Prices & Simple Moving Averages SMA(5 & 21)')
plt.show()

##########

# 5. Price Crossover Strategy Performance Comparison

# 5.1. Strategies Daily Returns
# Price Crossover Strategy Without Trading Commissions
spy['sma5drt'] = ((spy['Close']/spy['Close'].shift(1))-1)*spy['sma5str']
spy.iloc[0, 13] = 0
# Price Crossover Strategy With Trading Commissions (1% Per Trade)
spy['sma5str(-1)'] = spy['sma5str'].shift(1)
spy['sma5tc'] = spy['sma5sig']
sma5tc = 0
for i, r in enumerate(spy.iterrows()):
    if (r[1]['sma5sig'] == 1 or r[1]['sma5sig'] == -1) and r[1]['sma5str'] != r[1]['sma5str(-1)']:
        sma5tc = 0.01
    else:
        sma5tc = 0.00
    spy.iloc[i, 15] = sma5tc
spy['sma5drtc'] = (((spy['Close']/spy['Close'].shift(1))-1)-spy['sma5tc'])*spy['sma5str']
spy.iloc[0, 16] = 0
# Buy and Hold Strategy
spy['bhdrt'] = (spy['Close']/spy['Close'].shift(1))-1
spy.iloc[0, 17] = 0

# 5.2. Strategies Cumulative Returns
# Cumulative Returns Calculation
spy['sma5crt'] = np.cumprod(spy['sma5drt']+1)-1
spy['sma5crtc'] = np.cumprod(spy['sma5drtc']+1)-1
spy['bhcrt'] = np.cumprod(spy['bhdrt']+1)-1
# Cumulative Returns Chart
spy.plot(y=['sma5crt', 'sma5crtc', 'bhcrt'])
plt.title('Simple Moving Average SMA(5) vs Buy & Hold')
plt.legend(loc='upper left')
plt.show()

# 5.3. Strategies Performance Metrics
# Annualized Returns
sma5yrt = spy.iloc[251, 18]
sma5yrtc = spy.iloc[251, 19]
bhyrt = spy.iloc[251, 20]
# Annualized Standard Deviation
sma5std = np.std(spy['sma5drt'])*np.sqrt(252)
sma5stdc = np.std(spy['sma5drtc'])*np.sqrt(252)
bhstd = np.std(spy['bhdrt'])*np.sqrt(252)
# Annualized Sharpe Ratio
sma5sr = sma5yrt/sma5std
sma5src = sma5yrtc/sma5stdc
bhsr = bhyrt/bhstd
# Summary Results Data Table
data = [{'0': '', '1': 'SMA(5)', '2': 'SMA(5)TC', '3': 'B&H'},
        {'0': 'Annualized Return', '1': sma5yrt, '2': sma5yrtc, '3': bhyrt},
        {'0': 'Annualized Standard Deviation', '1': sma5std, '2': sma5stdc, '3': bhstd},
        {'0': 'Annualized Sharpe Ratio (Rf=0%)', '1': sma5sr, '2': sma5src, '3': bhsr}]
table = pd.DataFrame(data)
print(spy)
print(table)
