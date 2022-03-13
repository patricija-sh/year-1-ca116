#!/usr/bin/env python3

t = 0

i = 0
while i < 5:
   n = int(input())
   if n < 0:
      n = n * -1
      t = t + n
   else:
      t = t + n
   i = i + 1

print(t)
