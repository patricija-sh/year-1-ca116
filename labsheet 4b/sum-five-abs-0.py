#!/usr/bin/env python3

t = 0

n = int(input())
while n != 0:
   if n < 0:
      n = n * -1
      t = t + n
   else:
      t = t + n
   n = int(input())

print(t)
