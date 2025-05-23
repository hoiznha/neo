from konlpy.tag import Komoran

sentence = '코로나 바이러스 태블릿 PC,설진욱,가나다라'

print(' # before user dic')
komo = Komoran()
print(komo.pos(sentence))
print('-'*50)

komo = Komoran(userdic='user_dic.txt')
print(' # after user dic')
print(komo.pos(sentence))
print('-'*50)

print('# komo.nouns') #명사
result = komo.nouns(sentence)
print(result)
print('-'*50)

print('# komo.morphs') #형태소
result = komo.morphs(sentence)
print(result)
print('-'*50)

print('# komo.pos') #품사
result = komo.pos(sentence)
print(result)
print('-'*50)
