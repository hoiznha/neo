import json,urllib.request,datetime,math
import os.path
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import requests
import pandas as pd


BASE_DIR = os.path.dirname(os.path.dirname(os.path.relpath('./')))
secret_file = os.path.join(BASE_DIR, '../../secret.json')

with open(secret_file) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        errorMsg = 'Set the {} environment variable'.format(setting)
        return errorMsg

url = 'https://apis.data.go.kr/1352000/ODMS_COVID_02/callCovid02API'

#today = (datetime.today()-timedelta(days=1)).strftime('%Y%m%d'))
today = (datetime.today() - relativedelta(days=1)).strftime('%Y%m%d')
print(today)

params = '?serviceKey =' + get_secret('data_apiKey')
params += '&pageNo=1'
params += '&numOfRows=500'
params += '&apiType=JSON' 
params += '&status_dt=' + str(today)

url += params
print(url)

response = requests.get(url)
print(response)
print('-'*50)

contents = response.text
print(type(contents))  #string
print(contents) 
print('-'*50)

# dict = json.loads(contents)
# print(type(dict))
# print(dict)
# print('-'*50)

items = dict['items']
print(type(items))
print(items)
print('-'*50)

items_dict = { key : value for key,value in enumerate(items)}
print(type(items_dict))
print(items_dict)
print('-'*50)

items = items_dict[0]
print(type(items))
print(items)
print('-'*50)

validItem = {} #item 에 0이 아닌애들만 자동으로 담김 

for _ in item: 
    validItem[_] = items[_]
print(validItem)
print('-'*50)

df = pd.DataFrame.from_dict(validItem, orient='index').rename(columns={0:'result'})
print(type(df))
print(df)
print('-'*50)

item = df.loc[['gPntCnt','hPntCnt','accExamCnt','statusDt']]





data = df.loc[['gPntCnt','hPntCnt','accExamCnt','statusDt']]
print(type(data))
print(data)
print('-'*50)