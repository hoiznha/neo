#!/usr/bin/env python

import prime_func

n = int (input("enter a number : "))

while True:
    if (n == 0):
        break
    if (n < 2):
        print('re-enter number~!!')
        continue
    print ( f'{n}is prime number ') if prime_func.prime(n) == 1 else print(f'{n} is NOT prime number ')