import urllib.request, json

url = 'https://gist.githubusercontent.com/PrateekKumarSingh/ab456b5662a96d741ccbec72075d6cf4/raw/a044470e9aa47802e95f9e54e97109501f035769/example.json'

response = urllib.request.urlopen(url)
data = json.loads( response.read()) 

print(data)
