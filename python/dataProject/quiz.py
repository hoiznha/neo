#!/usr/bin/env python
#리스트 항목을 꺼내서 제곱값을 구해서 출력하는 제너레이터
from neo.python.dataProject.timer import timer

mynum = [1,2,3,4,5]

def square_number(nums):
    for i in nums:
        yield i*i

result = square_number(mynum)
for i in range(len(mynum)):
    print(f"square number : {mynum[i]} ^ {mynum[i]} : {next(result)}")
print(next(timer))

