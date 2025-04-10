#!/usr/bin/env python

class gcd(object):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __gcd__(self):
        print("gcd",self.a,self.b)
        while self.b != 0:
            r = self.a  % self.b
            self.a = self.b
            self.b = r
            print("gcd",self.a,self.b)
        return self.a

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

gcd1 = gcd(a,b)
print(f'gcd{a}, {b} of {a},{b} : {gcd1.gcd(a,b)}')