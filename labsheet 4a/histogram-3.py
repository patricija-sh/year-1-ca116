#!/usr/bin/env python3

histogram = ""
n = input()

i = 0
while i < len(n):
   histogram = "*" * int(n[i])
   print(histogram)
   i = i + 1
