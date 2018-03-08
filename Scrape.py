# import libraries
import urllib2
from bs4 import BeautifulSoup

# specify the url
quote_page = 'https://www.bloomberg.com/quote/SPX:IND'

page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")

name_box = soup.find('h1', attrs={'class': 'name'})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print name

# get the index price
price_box = soup.find('div', attrs={'class':'price'})
price = price_box.text
print price

