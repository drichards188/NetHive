from eod import EodHistoricalData
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import time
from termcolor import colored as cl
import mplfinance as mf
plt.style.use('fivethirtyeight')
plt.rcParams['figure.figsize'] = [20, 10]

# replace hardcode with .env
api_key = '<API_KEY>'
client = EodHistoricalData(api_key)

ticker = 'AAPL.US'
aapl_f_info = client.get_fundamental_equity(ticker)
aapl_f_info_keys = list(aapl_f_info.keys())
for i in range(len(aapl_f_info_keys)):
    print(cl(f'{i+1}. {aapl_f_info_keys[i]}', attrs = ['bold']))