#!/usr/bin/env python

def max(data):
    max_value = data[0]
    for i in range(len(data)):
        if data[i] > max_value:
            max_value = data[i]
    return max_value