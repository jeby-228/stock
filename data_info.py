'''
   Author  : Jeby 
   Date    : 2023.5.05
   Version : 1.0
   Description: Get the stock data transform to csv file
   History:
           1.0 : Get the stock data transform 
'''

import yfinance as yf
import os
stock_number = "0050.TW"
start_time = "2022-01-01"
end_time = "2023-05-07"
data = yf.download(stock_number ,
                   start=start_time,
                   end= end_time)

data.to_csv(f"{stock_number}-{start_time}_{end_time}"+".csv")



# print_out_string = f'''
#     {data[
#         [
#             data.keys()[0],
#             data.keys()[2],
#             data.keys()[3]
#         ]
#     ]}
#     {data.keys()[0]}
# '''

# print(print_out_string)


