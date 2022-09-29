#!/usr/bin/env python3
n = int(input()) 
a, b, c = map(int, input().split())

ans = 10000
for i in range(10000):
  for j in range(10000):
    rest = n - a*i - b*j
    k, mod = divmod(rest, c)
    if k >= 0 and mod == 0:
      ans = min(ans, i+j+k)

print(ans)

