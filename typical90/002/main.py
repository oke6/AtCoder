#!/usr/bin/env python3
n = int(input())

ans = []
for i in range(1<<n):
  count = 0
  temp = ''
  for j in range(n):
    if i & 1 << (n-1-j):
      temp += ')'
      count -= 1
    else:
      temp += '('
      count +=1

    if count < 0:
      break

  if count == 0:
    ans.append(temp)

ans.sort()
for x in ans:
  print(x)


