import json
import urllib.request
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1479032.json'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)
print(info['comments'])
# list comprehension
print(sum([item['count'] for item in info['comments']]))
