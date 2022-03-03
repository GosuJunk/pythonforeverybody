import urllib
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

maxVal = 7
url = 'http://py4e-data.dr-chuck.net/known_by_Dermot.html'
# also 'http://py4e-data.dr-chuck.net/comments_42.html' #input('Enter - ')
for i in range(0, maxVal):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    url = soup('li')[17]('a')[0].get('href', None)
    print(url)

# title = str(soup('title')[0].contents[0])
# url = re.findall('(www\..+)', title)[0]
#
#
# html = urlopen('http://' + url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")
# title = str(soup('title')[0].contents[0])
# print(title)
