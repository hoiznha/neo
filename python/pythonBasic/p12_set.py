#!/usr/bin/env python

even = set([0,2,4,6,8])
print(even)

hello = set('Hello')
print(hello)

s = even | hello
print(s)

p = even & hello
print(p)

hello.remove('e')
print(hello)

s1 = set([1,2,3,4,5])
s2 = set([4,5,6,7,8])

print(s1.intersection(s2))
print(s1 & s2)

print(s1.union(s2))
print(s1 | s2)

#difference
print(s1.difference(s2))
print(s1 - s2)

print(s2.difference(s1))
print(s2 - s1)

s3 = {1,2,3,4,5}

if s1==s2 :
    print("s1 = s2")
else :
    print("s1 does not equal s2")

if s1 ==s3 :
    print("s1 does not equal s3")

s4 = {6,7,8,9,10}

if s1.isdisjoint(s2):
    print("s1,s2 not have in common")
else:
    print("s1,s2 have in common")

if s3.isdisjoint(s4):
    print("s3,s4 not have in common")
else:
    print("s3,s4 have in common")

print(s1.issubset(s2))

s5 = {4,5}

print(s2.issubset(s5))
print(s5.issubset(s2))

s ={1,2,3}
print(f'set : {s}')

s.update({'a','b','c'})
print(f'set : {s}')

s.update([11,22,33])
print(f'set : {s}')

s.remove('a')
print(f'set : {s}')

s.discard('b')
print(f'set : {s}')

s= {'r','d','n','d','o','m'}
print(f'set : {s}')

print(f'set.pop() : {s.pop()}')
print(f'set : {s}')
print(f'set.pop() : {s.pop()}')
print(f'set : {s}')
print(f'set.pop() : {s.pop()}')
print(f'set : {s}')

s.clear()

s = {'a','b','c'}

if 'a' in s:
    print('a is exist')
else:
    print('a is not exist')

if 'z' in s:
    print('z is exist')
else:
    print('z is not exist')

print(f'length of set : {len(s)}')