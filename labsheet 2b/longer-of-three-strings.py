#!/usr/bin/env python3

s = input()
h = input()
i = input()

if len(s) > len(h) and len(s) > len(i):
   print(s)
elif len(h) > len(i):
   print(h)
else:
   print(i)
