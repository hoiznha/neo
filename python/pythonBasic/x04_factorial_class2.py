#!/usr/bin/env python

class factorial(object):
    def __init__(self,n):
        self.n = n
    def factorial(self):
        n = 1
        for i in range(1, self.n + 1) :
            n *= 1
        return n

a = int(input("Enter a number :"))
fact = factorial(a)
print(f'{a}! = {fact.factorial()}')