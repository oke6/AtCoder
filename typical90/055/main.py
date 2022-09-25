#!/usr/bin/env python3
from itertools import combinations

n, p, q = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i, j, k, l, m in combinations(a, 5):
  if i%p * j%p * k%p * l%p * m%p == q:
    ans += 1

print(ans)