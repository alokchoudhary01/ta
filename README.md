# Technical Analysis Library in Python

It is a Technical Analysis library to financial time series datasets (open, close, high, low, volume). You can use it to do feature engineering from financial datasets. It is builded on Python Pandas library.

![alt text](https://raw.githubusercontent.com/alokchoudhry01/ta/master/doc/figure.png)

The library has implemented 31 indicators:

#### Volume

* Accumulation/Distribution Index (ADI)
* On-Balance Volume (OBV)
* Chaikin Money Flow (CMF)
* Force Index (FI)
* Ease of Movement (EoM, EMV)
* Volume-price Trend (VPT)
* Negative Volume Index (NVI)

#### Volatility

* Average True Range (ATR)
* Bollinger Bands (BB)
* Keltner Channel (KC)
* Donchian Channel (DC)

#### Trend

* Moving Average Convergence Divergence (MACD)
* Average Directional Movement Index (ADX)
* Vortex Indicator (VI)
* Trix (TRIX)
* Mass Index (MI)
* Commodity Channel Index (CCI)
* Detrended Price Oscillator (DPO)
* KST Oscillator (KST)
* Ichimoku Kinkō Hyō (Ichimoku)

#### Momentum

* Money Flow Index (MFI)
* Relative Strength Index (RSI)
* True strength index (TSI)
* Ultimate Oscillator (UO)
* Stochastic Oscillator (SR)
* Williams %R (WR)
* Awesome Oscillator (AO)
* Kaufman's Adaptive Moving Average (KAMA)

#### Others

* Daily Return (DR)
* Daily Log Return (DLR)
* Cumulative Return (CR)


# Documentation

https://technical-analysis-library-in-python.readthedocs.io/en/latest/


# How to use (python 3.7)

```sh
$ pip install ta
```

To use this library you should have a financial time series dataset including "Timestamp", "Open", "High", "Low", "Close" and "Volume" columns.

You should clean or fill NaN values in your dataset before add technical analysis features.

#### Example adding all features

```python
import pandas as pd
import ta as ta

# Load datas
df = pd.read_csv('your-file.csv', sep=',')

# Clean NaN values
#df = utils.dropna(df)

# Add ta features filling NaN values
df = ta.add_all_ta_features(df, "Open", "High", "Low", "Close", "Volume_BTC", fillna=True)
```


#### Example adding individual features

```python
import pandas as pd
import matplotlib.pyplot as plt
import ta as ta

df = pd.read_csv('your-file.csv',sep=',')

print(df.columns)

# Add bollinger band high indicator filling Nans values
df['bb_high_indicator'] = ta.bollinger_hband_indicator(df["close"], n=20, ndev=2,fillna=True)

# Add bollinger band low indicator filling Nans values
df['bb_low_indicator'] = ta.bollinger_lband_indicator(df["close"], n=20, ndev=2,fillna=True)

print(df.columns)

df.plot()
plt.show()

```


# Deploy for developers

```sh
$ git clone https://github.com/alokchoudhry01/ta.git
$ cd ta
$ cd dev
$ python BollingerBandFeature.py
```


# Based on:

* https://en.wikipedia.org/wiki/Technical_analysis
* https://pandas.pydata.org

# TODO:

* add [more technical analysis features](https://en.wikipedia.org/wiki/Technical_analysis).
* automated tests for indicators.


# Credits:

Developed by Alok Choudhary contributors: https://github.com/alokchoudhry01/ta/

Please, let me know about any comment or feedback.

Also, I am a Software Consultant focused on Data Science using Python tools such as Pandas, Scikit-Learn, Backtrader. Don't hesitate to contact me if you need something related with this library, Python, Technical Analysis, AlgoTrading, Machine Learning, etc.
