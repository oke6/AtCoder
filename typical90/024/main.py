#!/usr/bin/env python3
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

diff = sum([abs(a[i]-b[i]) for i in range(n)])

if diff <= k and (diff+k)%2 == 0:
  print('Yes')
else:
  print('No')