# import libraries
import urllib2
from bs4 import BeautifulSoup

quote_page = "https://finance.yahoo.com/portfolio/p_0/view/v1"

page = urllib2.urlopen(quote_page)
soup = BeautifulSoup(page, "html.parser")

name_box = soup.find(attrs={'class': '_2Aw8c'})

name = name_box.text.strip() # strip() is used to remove starting and trailing
print name

# get the index price
price_box = soup.find('div', attrs={'class':'_2Aw8c'})
price = price_box.text
print price