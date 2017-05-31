import requests
from   bs4 import BeautifulSoup
from bs4 import UnicodeDammit
import re
import csv

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
        temp = tag.text 
        temp = temp.strip('\n')
        temp_parts = temp.split('\n')
        player_name, player_id = temp_parts[0].split('#')
        print('\t', player_name, player_id)
        with open("Teamlist final.csv", "w", encoding='utf-8') as file_handler:
            file_handler.write('/n {}'.format(teamname.text))
            file_handler.write('{}#{}'.format(player_name, player_id))
    

