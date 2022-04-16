import pandas as pd
import numpy as np
import datetime
from datetime import datetime
from datetime import date
import pandasql as ps
import MetaTrader5 as mt5
import time
from time import sleep
from subprocess import call
import matplotlib.pyplot as plt
import pandasql as ps
import talib
from talib import RSI, EMA


#Account Set Up /Configuración de la Cuenta

name = 123746535 #The account Number
key = "Inup.2020" #The account key
serv = "Pepperstone-MT5-Live01" #The server of your account
path = r"C:\Program Files\MetaTrader 5 B\terminal64.exe" #The folder where the MT5.exe is located
symbol = "EURUSD" #The symbol you want the data

#mt5.initialize() establishes the connection with MT5. Here we pass the access keys anad the path
mt5.initialize( login = name, server = serv, password = key, path = path)

#First we get the last 1000 candlestick using the 1 hour data
rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_H1, 0, 1000)

#With these rates, then we create the dataframe with the organized columns
rates_frame = pd.DataFrame(rates)

#Finally we transform the Time column into a Timestamp column
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
