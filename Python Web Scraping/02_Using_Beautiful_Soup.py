import requests, string
from bs4 import BeautifulSoup

baseURL = 'https://github.com/'
github_repo = {}

# requesting the web URL
page = requests.get("https://github.com/trending/powershell")
soup = BeautifulSoup(page.content,'html.parser')
#print(soup.prettify()) # Parses the content and a readable format
li_tags = soup.find_all('li',{"class": "col-12 d-block width-full py-4 border-bottom"})
for li in li_tags:
    div_tags = li.find_all('div', {"class": "d-inline-block col-9 mb-1"})
    for div in div_tags:
        reponame = div.get_text().strip().replace(" ", "")

        github_repo["Repo"]=reponame
        github_repo["RepoURL"]="https://github.com/"+reponame

    div_tags = li.find_all('div', {"class": "py-1"})
    for div in div_tags:
        description = div.get_text().strip()
        github_repo["Description"]=description

    div_tags = li.find_all('div', {"class": "f6 text-gray mt-2"})

    for div in div_tags:
        a_tags = div.find_all('a', {"class": "muted-link d-inline-block mr-3"})
        github_repo['StargazersURL']=baseURL+a_tags[0]['href']
        github_repo['StargazersCOunt']=a_tags[0].get_text().strip()
        github_repo['Forks']=baseURL+a_tags[1]['href']
        github_repo['ForksCount']=a_tags[1].get_text().strip()

        span = div.find_all('span', {"class": "d-inline-block float-sm-right"})
        for s in span:
            github_repo['StarsThisMonth']=s.get_text().strip()

print(github_repo)
