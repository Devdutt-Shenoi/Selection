#!/bin/python3

s = input().strip()
c=1
for i in s:
   if(i.isupper()):
        c+=1
print(c)
