#!/bin/python3

import sys

def solve(n, p):
    d=n//2-p//2
    a=min(d,p//2)
    return a
n = int(input().strip())
p = int(input().strip())
result = solve(n, p)
print(result)
