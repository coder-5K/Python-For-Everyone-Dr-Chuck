# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

from urllib.request import urlopen
from bs4 import BeautifulSoup
import sslC
import re

# Ignores SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')                      # request user to input url of a website
html = urlopen(url, context=ctx).read()      # variable HTML is assigned the content of the url variable and is read into a string
#print(html)
soup = BeautifulSoup(html, "html.parser")    #BeautifulSoup makes the variable HTML look nice and pretty and assigns it to SOUP
total_sum = 0
#print(soup)

tags = soup('span')                          #puts all the lines with 'span' in them into a [LIST] called 'tags'

#print(tags)

for tag in tags:
   # Look at the parts of a tag
   #print ('TAG:',tag)
   #print ('URL:',tag.get('href', None))
   #print ('Contents:',tag.contents[0])
   #print ('Attrs:',tag.attrs)
   total_sum = total_sum + int(tag.contents[0])

print(total_sum)




