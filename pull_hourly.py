import pandas as pd
import requests
import os
import logging
# Pulling data from cryptocompare API
URL = 'https://min-api.cryptocompare.com/data/histohour'

def get_hourly(ticker):
    params = {'fsym': ticker,
              'tsym': 'USD',
              'limit': 2001,
              'aggregate': 1}
    resp = requests.get(url=URL, params=params)

    try:
        df = pd.DataFrame(resp.json()['Data'])
        return df
    except:
        raise Exception('Failed to get data, m8')

tickerlist=['BTC', 'ETH', 'LTC', 'XRP', 'BCH', 'STRAT', 'DASH', 'NEO', 'ETC', 'XMR', 'BCC', 'OMG', 'PAY', 'WAVES', 'EOS', 'BTS', 'ZEC', 'USDT', 'STEEM', 'BCN', 'ICN', 'GNT', 'VERI', 'SNT' ] 

#if os.path.exists('data'):
#    os.remove('data')
for ticker in tickerlist:
    #logging.info('pulling data for %s', ticker)
    print('pulling data for %s'%ticker)
    df = get_hourly(ticker)
    filepath=os.path.join(os.getcwd(),'data/'+ticker+'.csv')

    df.to_csv(filepath,index=False)
