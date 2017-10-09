import urllib.request, urllib.parse, re

url = 'http://geekeefy.wordpress.com'

req = urllib.request.Request(url) # create a webrequest
resp = urllib.request.urlopen(req) # web request and capture the response
respdata = resp.read() # read the response data

hyperlinks = re.findall(r'<a href="(.*?)"',str(respdata)) # regex to parse and capture all hyperlinks
paragraph = re.findall(r'<p>(.*?)</p>',str(respdata)) # regex to parse and capture all paragraph

# print all hyperlinks captured
for link in hyperlinks:
    print(link)

#print(hyperlinks[0:10]) # print first 10 hyperlinks 
#print(paragraph[0:4]) # print first 4 paragraphs


