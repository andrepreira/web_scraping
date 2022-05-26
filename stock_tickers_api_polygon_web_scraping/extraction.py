import requests
import pandas as pd
import json
import time


def return_common_stock_tickers(token, limit):
    url = 'https://api.polygon.io/v3/reference/tickers'
    
    parameters = {
        'apiKey': token, # your API key
        'type': 'CS', # query common stocks
        'market': 'stocks',
        'limit': limit # extract max data possible
    }
    
    try:
        tickers_json = requests.get(url,parameters).json()
        tickers_list = tickers_json['results']
        
        while tickers_json['next_url']:
            tickers_json = requests.get(tickers_json['next_url'], parameters).json()
            tickers_list.extend(tickers_json['results'])
            if 'next_url' not in tickers_json.keys():
                break
            #trigger a wait since free tier is limited to 5 call/min
            time.sleep(12)
    except:
        return None
    
    return tickers_list


token = 'g7oqY65Zga_2yQYF4ppZl5Yf6v5vLaMX'

tickers = return_common_stock_tickers(token, 1000)
print(tickers)

# write out as csv

df_cs_tickers = pd.DataFrame(tickers)
print(df_cs_tickers)
df_cs_tickers.to_csv('polygon_cs_tickers.csv')

# write out as text

with open('polygon_cs_tickers.txt', 'w') as outfile:
    json.dump(tickers, outfile, indent=4)