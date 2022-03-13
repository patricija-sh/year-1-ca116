#!/usr/bin/env python3

n = int(input())
m = int(input())

while i < n:
   if (m % 2 == 0):
      print(m // 2)
   else:
      print((m * 3) + 1)
   i = i + 1
