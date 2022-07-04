import urllib.request
from bs4 import BeautifulSoup

url = 'https://music.bugs.co.kr/chart/'

res = urllib.request.urlopen(url)
soup = BeautifulSoup(res,'lxml')

title = []
result = soup.select('p.title > a')
for item in result:
    title.append(item.string)
# print(title)

singer = []
result = soup.select('p.artist > a:nth-of-type(1)')
for item in result:
    singer.append(item.string)
# print(singer)

print(list(zip(title,singer)))