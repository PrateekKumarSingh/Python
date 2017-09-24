import urllib.request
import urllib.parse

#webrequest = urllib.request.urlopen('http://www.geekeefy.wordpress.com')
#print(webrequest.read())

url = "https://geekeefy.wordpress.com"
dic = {'s':'Microsoft API'} # dictionary with url search parameters "https://geekeefy.wordpress.com/s=MicrosoftAPI"

data = urllib.parse.urlencode(dic) # Encoded your URL, so thing like space will become %20 or + which is a WWW standard
data = data.encode('utf-8')
print('Encoded data:',data.decode())

request = urllib.request.Request(url, data)  # Make a web request with URL and encoded data
resp = urllib.request.urlopen(request) # Web request using the request variable = URL+Data
print(resp.read()) # To read the web response recieved












