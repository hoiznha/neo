#!/usr/bin/env python

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

a = int(input("Enter a number :"))
print(f'{a}! = {factorial(a)}')