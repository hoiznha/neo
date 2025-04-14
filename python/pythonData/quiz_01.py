from bs4 import BeautifulSoup
from pandas import DataFrame as df
import numpy as np


html = open("/work/neo/html/source/5/ex5-10.html",'r',encoding='utf-8')
soup = BeautifulSoup(html,'html.parser')
table = soup.select_one('table')
tbody = table.select_one('tbody')
tds = tbody.find_all('td')

print(tds)

list = []

for data in tds:
    list.append(data.text)
print(list)

mycolumns = ['이름','국어','영어']

myframe = df(np.reshape(np.array(list),(4,3)),columns=mycolumns)
myframe = myframe.set_index('이름')
print(myframe)

