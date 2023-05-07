import yfinance as yf
import talib
import matplotlib.pyplot as plt

# 下載股票資料
symbol = '0050.TW'
data = yf.download(symbol, start='2023-01-01', end='2023-05-07')

# 計算布林通道指標
upperband, middleband, lowerband = talib.BBANDS(
    data['Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)

# 繪製股價走勢和布林通道
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(data['Close'], label='Close')
ax.plot(upperband, label='Upper Band')
ax.plot(middleband, label='Middle Band')
ax.plot(lowerband, label='Lower Band')
ax.legend(loc='best')
plt.title(F"{symbol} Bollinger Band Chart")
ax.set_xlabel('Date')
ax.set_ylabel('Price')
plt.savefig(f"{symbol}_BBAND.png")
plt.show()