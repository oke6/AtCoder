#!/usr/bin/env python3
def gcd(x, y):
  if (y == 0):
    return x
  else:
    return gcd(y, x%y)

a, b, c = map(int, input().split())
gcd = gcd(gcd(a,b),c)

a //= gcd
b //= gcd
c //= gcd

print(a+b+c-3)
