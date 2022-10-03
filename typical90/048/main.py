#!/usr/bin/env python3
n, k = map(int, input().split())

scores = []

for _ in range(n):
  a, b = map(int, input().split())
  scores.append(b)
  scores.append(a-b)

scores.sort(reverse=True)
print(sum(scores[0:k]))
  


