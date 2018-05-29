from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import sys
import quandl

ticker = sys.argv[1]

print "Pulling stock information from ticker ", ticker, "."
print "The purpose of this pull is a 50 day moving average analysis." 
print "This is to get more information on when to buy in on the expansion stage of a stock.\n"

style.use('ggplot')

end = datetime.now()
start = end - timedelta(days=50)
print start
print end
result = quandl.get("NASDAQOMX/COMP-NASDAQ", start_date='2018-01-01', end_date='2018-05-01')

print(result.head())
