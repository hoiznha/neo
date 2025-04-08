#!/usr/bin/env python

#f(x) = f(x-1) + f(x-2)

num =1
prev =0
cur =1

print("%3d : %d" % (num, next))
while num <10:
    next = cur + prev
    prev = cur
    cur = next
    num += 1