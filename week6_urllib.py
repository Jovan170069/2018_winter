import urllib.request
with urllib.request.urlopen('http://google.com/') as response:
   html = response.read()
   print(html)
