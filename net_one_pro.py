'''
   Author  : Jeby
   Date    : 2023.5.08
   Version : 1.0
   Description: BBAND 
   History:
           1.0 : Get the stock data transform
'''


# -*- coding: UTF-8 -*-
import yfinance as yf
import datetime
import talib
import matplotlib.pyplot as plt
from pandas import DataFrame

class Stock():
    def __init__(self,
                 stock_id: str = "0050.TW",
                 start_date: str = "2022-01-01"):

           self.start_time = start_date
           self.end_date = datetime.datetime.now().date().strftime('%Y-%m-%d')

           self.stock_id = stock_id

           self._data = yf.download(self.stock_id,
                                    start=self.start_time,
                                    end=self.end_date)

           self.close = self._data['Close']

    def BB(self, MA_days: int = 10):
        '''
        return : MA DAYS
        '''
        self._upperband, self._middleband, self._lowerband = talib.BBANDS(
            self.close, timeperiod=MA_days, nbdevup=2, nbdevdn=2, matype=0)
        return MA_days
    
    def out_upperband(self):
        '''Returns the BBAND upper band '''
        return self._upperband

    def out_middleband(self):
        '''Returns the BBAND middle band '''
        return self._middleband

    def out_lowerband(self):
        '''Returns the BBAND lower band '''
        return self._lowerband


    def graph(self, show: bool = True):
        '''
        perm_1 : show out graph

        Returns the graph and save graph        
        '''
        fig, ax = plt.subplots(figsize=(10, 5))

        ax.plot(self._data['Close'], label='close')
        ax.plot(self._upperband, label='upper band')
        ax.plot(self._middleband, label='middle')
        ax.plot(self._lowerband, label='low band')
        ax.legend(loc='best')
        ax.set_xlabel('date')
        ax.set_ylabel('price')

        plt.title(f"{self.stock_id} bollinger Band Chart")
        plt.savefig(f'BB_photo/{self.stock_id}--BBAND.png')
        if show:
            plt.show()


    

if __name__ == "__main__":
        s = Stock(stock_id='2330.TW', start_date='2023-01-09')
        s.BB()
        print(type(s.out_lowerband()))
        # s.graph(show =False)
