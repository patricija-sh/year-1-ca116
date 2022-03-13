#!/usr/bin/env python3

amount = int(input())
histogram = ""

i = 0
while i < amount:
   n = int(input())
   histogram = "*" * n
   print(histogram)
   i = i + 1
