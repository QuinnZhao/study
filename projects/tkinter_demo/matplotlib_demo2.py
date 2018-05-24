import talib
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt
import mpl_finance as mpf

data = ts.get_k_data('399300', index=True, start='2017-01-01', end='2017-06-31')
sma_10 = talib.SMA(np.array(data['close']), 10)
sma_30 = talib.SMA(np.array(data['close']), 30)

fig, (ax, ax2) = plt.subplots(2, 1, sharex=True, figsize=(17, 10))

mpf.candlestick2_ochl(ax, data['open'], data['close'], data['high'], data['low'],
                     width=0.5, colorup='r', colordown='green', alpha=0.6)

ax.set_xticklabels(data['date'][::10])
ax.plot(sma_10, label='SMA 10')
ax.plot(sma_30, label='SMA 30')
ax.legend(loc='upper left')
ax.grid(True)

data['volume'].plot(kind='bar', color='k', alpha=0.3)
ax2.set_xticks(range(0, len(data['date']), 10))
ax2.set_xticklabels(data['date'][::10], rotation=30)
ax2.grid(True)

plt.subplots_adjust(hspace=0)
plt.show()