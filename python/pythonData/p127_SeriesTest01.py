from pandas import Series

mylist = [10,40,30,40]
myseries = Series(data=mylist, index=['김유신','이순신','강감찬','광해군'])

print('\n Data Type')
print(type(myseries))

myseries.index.name = '점수'
print('\n Index Name of series')
print(myseries.index.name)

print('\n Name of Index')
print(myseries.index)

print('\n Value of series')
print(myseries.values)

print('\nprint information of Series')
print(myseries)

print('\n Repeat of print')
for idx in myseries.index:
    print('index : ' + idx + ', value : ' + str(myseries[idx]))
