import talib
import yfinance as yf
import matplotlib.pyplot as plt

symbol = "0050.TW"
df = yf.Ticker(symbol).history(period='max')

# print("df\n", df)
# 利talib函式庫之BBANDS函式計算布林通道（上軌、中軌、下軌）
upperband, middleband, lowerband = talib.BBANDS(
    df.Close, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
# print(upperband, middleband, lowerband)

print("upperband\n", upperband)
print("middleband\n", middleband)
print("lowerband\n", lowerband)
plt.plot(upperband['2023-1-1':'2023-5-5'],
         label="upperband", color='r',
         linestyle='solid')
plt.plot(middleband['2023-1-1':'2023-5-5'],
         label="middleband", color='g', linestyle='solid')
plt.plot(lowerband['2023-1-1':'2023-5-5'],
         label="lowerband", color='b',
         linestyle='solid')
plt.title(F"{symbol} Bollinger Band Chart")
plt.xlabel("Day")
plt.ylabel("Bollinger Band")
plt.savefig("BBAND.png")
