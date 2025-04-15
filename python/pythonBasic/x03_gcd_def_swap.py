#!/usr/bin/env python


a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

def gcd(a,b):
    if a < b:
        a,b = b,a
        print("gcd",(a,b))
    while b != 0:
        r = a % b
        a = b
        b = r
        print("gcd", a,b)
    return a

print(f'gcd(a,b) = {gcd(a,b)}')



