#!/usr/bin/env python3

n = int(input())
pos_total = 0
neg_total = 0

while n != 0:
   if n > 0:
      pos_total = pos_total + n
   else:
      neg_total = neg_total + n
   n = int(input())

print(neg_total, pos_total)
