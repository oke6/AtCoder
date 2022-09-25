#!/usr/bin/env python3
def eight_to_ten(n):
  eight = str(n)
  l = len(eight)
  p = 1
  ret = 0
  for i in range(l):
    ret += int(eight[l-1-i])*p
    p *= 8
  return ret

def ten_to_nine(n):
  if n == 0:
    return 0
  ret = ''
  while n > 0:
    ret = str(n%9) + ret
    n //= 9
  return int(ret)


n, k = map(int, input().split())

ans = n
for _ in range(k):
  ans = int(str(ten_to_nine(eight_to_ten(ans))).replace('8', '5'))

print(ans)




