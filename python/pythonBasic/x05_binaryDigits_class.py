#!/usr/bin/env python

import random

from neo.python.pythonBasic.x05_binaryDigits_def import binaryDigits


class BinaryDigits(object):
    def __init__(self,num,lists):
        self.num = num
        self.lists = lists

    def __convert__(self):
        n = self.num
        while True:
            r = n % 2
            q = n // 2
            lists.append(r)
            if q == 0:
                break
        lists.reverse()
        return lists

lists = []
num = random.randrange(4, 20)
binary = BinaryDigits(num,lists)
print(f'{num} binary number is : {binary.__convert__()}')


