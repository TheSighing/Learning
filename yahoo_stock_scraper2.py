import urllib2
from bs4 import BeautifulSoup
import re

htmlfile = urllib2.urlopen("http://finance.yahoo.com/q?s=AAPL")

htmltext = htmlfile.read()

soup = BeautifulSoup(htmltext, "html.parser")
#print soup
# Get the sub url ie /quote/AAPL/history?p=AAPL to get th ehistorical data on a stock

for price in soup.find_all("span", text=re.compile("Previous Close")):
    print (price.parent.text)
    print (price.parent.findNext('td').text)
# for price in soup.find_all(id="quote-summary"):
#     print (price.find_all(text="Previous Close"))

