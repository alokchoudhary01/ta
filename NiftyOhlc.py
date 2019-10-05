import pandas as pd
import matplotlib.pyplot as plt

file = 'C:\\Users\\user\\niftyohlc.csv'

# Read file from local system
data = pd.read_csv(file)
#data = pd.read_csv(file,parse_dates=True,index_col=0)

print(data[['date','open','high']].head(5))
print(data[['date','open','high']].tail(5))

data['close'].plot()
plt.show()


