import requests
from   bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import re

linklist = []
taglist = []
x = 0

while x <= 28:
    url = 'https://www.overwatchcontenders.com/teams/index/EU?page={}&search='.format(x)
    raw = requests.get(url)
    soup = BeautifulSoup(raw.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        a = str(a['href'])
        if a.startswith('/teams/details/') == True:
            linklist.append(a)
    x = x + 1

for link in linklist:
    teamurl = 'https://www.overwatchcontenders.com{}'.format(link)
    source = requests.get(teamurl)
    soup = BeautifulSoup(source.text, 'html.parser')
    teamname = soup.find("h2", {"class": "team-name"})
    print(teamname.text)
    for tag in soup.find_all("div", {"class": "battletag"}):
        temp = tag.text.encode('utf-8')
        #finaltag = re.search("b'\\n(.*)\\n\(Europe\)\\n'", battletag)
        print(temp)
