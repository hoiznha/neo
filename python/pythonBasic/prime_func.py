#!/usr/bin/env python

def prime(n):
    for i in range (2,n+1):
        if n % i == 0:
            break
        if n == i:
            return 1
        else :
            return 0
