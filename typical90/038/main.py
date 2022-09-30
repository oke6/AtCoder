def GCD(x, y):
  if y == 0:
    return x
  return GCD(y, x%y)
 
a, b = map(int, input().split())
gcd = GCD(a, b)
ans = a*b//gcd
 
if ans > 10**18:
  print('Large')
else:
  print(ans)
