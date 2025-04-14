from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "http://www.cgv.co.kr/movies/?lt=1&ft=0"

data = requests.get(url)
soup = BeautifulSoup(data.text, "html.parser")

print(soup.select_one('title').string)

infos = soup.find_all('div',attrs={'class':'sect-movie-chart'})

mydata0 = [i for i in range(1,20)]

result = []
title = soup.select('strong.title')
for i in title :
    result.append(i.text)
mydata1 = result
# print(mydata1)

result=[]
score = soup.select("span.percent")
for i in score:
    result.append(i.text)
mydata2 = result
# print(mydata2)

result= []
reserv = soup.select("strong.percent")
for i in reserv:
    result.append(i.text.lstrip("예매율"))
mydata3 = result
# print(mydata3)

result = []
release = soup.select("span > strong")
for i in release:
    result.append(i.text.strip()[0:10])
mydata4 = result

mycolumn = ['순위','제목','평점','예매율','개봉일']

myframe = pd.DataFrame(data=list(zip(mydata0,mydata1,mydata2,mydata3,mydata4)),columns=mycolumn)
myframe = myframe.set_index(keys=['순위'])
print(myframe)
print('-'*40)

filename = 'quiz_02_cgvMovie.csv'



