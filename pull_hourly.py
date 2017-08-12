import pandas as pd
import requests
import os
# Pulling data from cryptocompare API
URL = 'https://min-api.cryptocompare.com/data/histohour'

def get_hourly(ticker):
    params = {'fsym': ticker,
              'tsym': 'USD',
              'limit': 60,
              'aggregate':3}
    resp = requests.get(URL, params)

    try:
        df = pd.DataFrame(resp.json()['Data'])
        return df
    except:
        raise Exception('Failed to get data, m8')

for ticker in ['BTC', 'ETH']:
    tmp = get_hourly(ticker)
        os.removedirs('data')
