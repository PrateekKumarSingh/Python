import requests
from bs4 import BeautifulSoup    

# requesting the web URL
page = requests.get("http://www.geekeefy.wordpress.com")
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.prettify()) # Parses the content and a readable format

print(soup.find_all('p')[2])
print(soup.find_all('p')[2].get_text())
print(soup.find_all('p'))


