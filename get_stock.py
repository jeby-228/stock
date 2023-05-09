'''
   Author  : Jeby
   Date    : 2023.5.07
   Version : 1.0
   Description: Get the stock data transform to csv file
   History:
           1.0 : Get the stock data transform
'''
# -*- coding: UTF-8 -*-
import yfinance as yf
import datetime
import os

# START_DATE = "2022-01-01"

def get_stock_to_csv(stock_id :str= "0050.TW" ,start_date: str = "2022-01-01") -> str:
        '''
        var 1 : stock_id -> string，股票代碼，預設為"0050.TW"
        var 2 : start_data -> string re(yyyy-mm-dd)，數據的開始日期，預設為"2022-01-01"

        return :csv file name，返回生成的CSV檔案名稱
        
        csv file info : Open,High,Low stock data
        '''
        
        stock_folder = "stock_pool"
        now = datetime.datetime.now()
        stock_number = stock_id
        start_time = start_date
        end_time = now.date().strftime('%Y-%m-%d')

        data = yf.download(stock_number ,
                   start=start_time,
                   end= end_time)

        input_to_csv =  data[ [  "Open" , "High" , "Low"  ] ]
        filename = f"{stock_number}-start_date{start_time}"+".csv"

        input_to_csv.to_csv(f"{stock_folder}/{filename}")

        return filename


if __name__ == "__main__":
        get_stock_to_csv()
        pass

