#!/usr/bin/env python3
n, m = map(int, input().split())

A = [ [] for _ in range(n) ]

for _ in range(m):
  a, b = map(int, input().split())
  A[max(a, b)-1].append(min(a, b)-1)

ans = 0
for a in A:
  if len(a) == 1:
    ans += 1

print(ans)