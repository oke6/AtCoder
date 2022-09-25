#!/usr/bin/env python3
n = int(input()) 

s = set()
for i in range(n):
  name = input()
  if not name in s:
    print(i+1)
    s.add(name)



