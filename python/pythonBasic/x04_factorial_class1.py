#!/usr/bin/env python

class factorial(object):
    def __init__(self,n):
        self.n = n
    def factorial(self):
        if self.n == 0 :
            return 1
        else :
            n = self.n
            self.n -= 1
            return n * self.factorial()

a = int(input("Enter a number :"))
fact = factorial(a)
print(f'{a}! = {fact.factorial()}')