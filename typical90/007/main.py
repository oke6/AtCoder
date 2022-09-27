#!/usr/bin/env python3

def is_ok(arg, val):
  return a[arg] > val

def meguru_bisect(ng, ok, val):
  while (abs(ok - ng) > 1):
    mid = (ok + ng) // 2
    if is_ok(mid, val):
      ok = mid
    else:
      ng = mid
  return ok


n = int(input())
a = list(map(int, input().split()))
q = int(input())

a.sort()
for _ in range(q):
  b = int(input())
  pos = meguru_bisect(-1, n-1, b)
  if 0 < pos:
    print(min(abs(b-a[pos]), abs(b-a[pos-1])))
  else:
    print(abs(b-a[pos]))


