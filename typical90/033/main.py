#!/usr/bin/env python3
from curses import has_colors


h, w = map(int, input().split())

if h == 1:
  print(w)
elif w == 1:
  print(h)
else:
  row = (w+1)//2
  col = (h+1)//2
  print(row*col)