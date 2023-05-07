import twstock


# data = twstock.realtime.get("0050")
stock = twstock.Stock("0050")
start_date = '2023-01'
end_date = '2023-05'
data = stock.fetch_from(2023,2).__len__()

print(data)



