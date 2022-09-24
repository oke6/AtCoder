#!/usr/bin/env python3
h, w = map(int, input().split())
a = [ list(map(int, input().split())) for _ in range(h) ]

row = []
col = []

for i in range(h):
  row.append(sum(a[i]))

for j in range(w):
  col.append(sum(a[i][j] for i in range(h)))

for i in range(h):
  ans_row = []
  for j in range(w):
    ans_row.append(row[i]+col[j]-a[i][j])
  
  print(*ans_row)

