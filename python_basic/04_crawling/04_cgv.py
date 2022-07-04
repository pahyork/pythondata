import urllib.request
from bs4 import BeautifulSoup
import requests

url = 'https://www.cgv.co.kr/movies/'

res = requests.get(url).text
soup = BeautifulSoup(res,'lxml')
# print(soup.prettify())

result = soup.select('strong.title')
# print(result)

movieName = []
for item in result:
    movieName.append(item.string)
# print(movieName)

imgUrl = []
result = soup.select('span.thumb-image img')
for item in result:
    imgUrl.append(item['src'])
# print(imgUrl)
print(list(zip(movieName,imgUrl)))