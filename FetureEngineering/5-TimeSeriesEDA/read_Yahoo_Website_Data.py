import time
import datetime
import pandas as pd

ticker = 'TSLA'
period1 = int(time.mktime(datetime.datetime(2018, 1, 1, 1, 59).timetuple()))

''' 
mktime() method of Time module is used to convert a time. struct_time object or a tuple containing 9 elements corresponding 
to time. struct_time object to time in seconds passed since epoch in local time. This method is the inverse function of time

timetuple() returns the time. struct_time() object as a tuple that contains the date and time information, i.e., timestamps. 
Note: This method is part of the time module and thus returns the object of time .
'''

period2 = int(time.mktime(datetime.datetime(2023, 1, 1, 1, 59).timetuple()))
interval = '1d' # 1wk, 1m

query_String = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

df = pd.read_csv(query_String)

# print(df)
df.to_csv('TSLA.csv')  # the file is generated in root directory - change directory to get files generated
