#!/usr/bin/env python

n = int(input("How much number input? :"))

building = list(map(int,input().split()))
print("\nbuilidng : ", building)

min_build = min(building)
print("min(building) : ", min_build)

min_build_num =  min_build * n
print("min_build * n : ", min_build_num)

sum_building = sum(building)
print("\nsum(building) : ", sum_building)

result = sum_building - min_build_num
print("\nsum(building) - (min_build * n) : ", result)

